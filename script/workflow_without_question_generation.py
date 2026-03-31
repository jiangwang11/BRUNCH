import os
import re
import subprocess
import sys
from dataclasses import dataclass
from dotenv import load_dotenv


def sanitize_model_dir_name(model_name: str) -> str:
    normalized = model_name.replace("/", "_")
    return re.sub(r'[\\/*?:"<>|]', "_", normalized)[:80].strip()


@dataclass
class WorkflowConfig:
    student_model: str = "qwen/qwen3-8b"
    problem_generation_model: str = "openai/gpt-4o-mini"
    teacher_model: str = "qwen/qwen3-8b"
    dataset_name: str = "test_workflow"
    paper_csv_path: str = "data/papers.csv"
    paper_name_column: str = "title"
    num_to_process: int = 4
    survey_model: str = "qwen/qwen3-8b"
    field_model: str = "openai/gpt-5-mini"
    survey_batch_size: int = 10
    check_paper_test_limit: int = 10
    llm_judge_input_json: str = "short_answer.json"
    llm_judge_start_index: int = 0
    llm_judge_end_index: int = 10
    stop_on_error: bool = True

    def to_env(self, script_dir: str) -> dict:
        survey_dir_name = sanitize_model_dir_name(self.survey_model)
        output_root = os.path.join(script_dir, "output")
        
        # We directly use the provided files instead of generating them
        filter_output_json = os.path.join(output_root, "openai_batch_output.filtered.json")
        fields_output_json = os.path.join(output_root, "paper_fields_output.json")
        
        # Subsequent output files can still be placed in dataset specific folder if preferred,
        # or kept in output_root. We'll put new outputs in output/test_workflow
        dataset_root = os.path.join(output_root, self.dataset_name)
        os.makedirs(dataset_root, exist_ok=True)
        
        check_paper_output_json = os.path.join(dataset_root, f"survey_check_result_{survey_dir_name}.json")
        
        base_env = dict(os.environ)
        api_key = (base_env.get("API_KEY") or "").strip()
        openrouter_key = (base_env.get("OPENROUTER_KEY") or "").strip()
        if not api_key and openrouter_key:
            base_env["API_KEY"] = openrouter_key
        if not openrouter_key and api_key:
            base_env["OPENROUTER_KEY"] = api_key
        base_env.update(
            {
                "PYTHONIOENCODING": "utf-8",
                "PROBLEM_API_BASE_URL": "https://openrouter.ai/api/v1",
                "FILTER_API_BASE_URL": "https://openrouter.ai/api/v1",
                "FIELD_API_BASE_URL": "https://openrouter.ai/api/v1",
                "SURVEY_API_BASE_URL": "https://openrouter.ai/api/v1",
                "CHECK_PAPER_API_BASE_URL": "https://openrouter.ai/api/v1",
                "LLM_JUDGE_API_BASE_URL": "https://openrouter.ai/api/v1",
                "STUDENT_MODEL": self.student_model,
                "TEACHER_MODEL": self.teacher_model if self.teacher_model != "__YOUR_TEACHER_MODEL__" else "",
                "DATASET_NAME": self.dataset_name,
                "PAPER_CSV_PATH": self.paper_csv_path,
                "PAPER_NAME_COLUMN": self.paper_name_column,
                "NUM_TO_PROCESS": str(self.num_to_process),
                # We skip problem, filter, clean, fields generation.
                # So we just provide what the subsequent scripts need.
                "FIELDS_OUTPUT_JSON": fields_output_json,
                "SURVEY_MODEL": self.survey_model,
                "SURVEY_HEALTH_CHECK_MODEL": self.survey_model,
                "SURVEY_BATCH_SIZE": str(self.survey_batch_size),
                "SURVEY_ROOT_DIR": dataset_root,
                "TARGET_SURVEY_DIR_NAME": survey_dir_name,
                "CHECK_PAPER_JSON_PATH": filter_output_json,
                "CHECK_PAPER_OUTPUT_PATH": check_paper_output_json,
                "CHECK_PAPER_TEST_LIMIT": str(self.check_paper_test_limit),
                "SOLVE_API_BASE_URL": "https://openrouter.ai/api/v1",
                "SOLVE_MODEL": self.student_model,
                "SOLVE_INPUT_JSON": filter_output_json,
                "SOLVE_OUTPUT_JSON": os.path.join(dataset_root, f"survey_direct_compare_result_{survey_dir_name}.json"),
                "SOLVE_TEST_LIMIT": str(self.check_paper_test_limit),
                "CHECK_PERCENTAGE_INPUT_JSON": check_paper_output_json,
                "CANDIDATE_MODELS": self.student_model,
                "CANDIDATE_SURVEY_DIRS": survey_dir_name,
                "LLM_JUDGE_INPUT_JSON": self.llm_judge_input_json,
                "LLM_JUDGE_FINAL_RESULT_JSON": os.path.join(dataset_root, f"final_result_{self.dataset_name}.json"),
                "LLM_JUDGE_OUTPUT_DIR": os.path.join(dataset_root, "llm_judge"),
                "LLM_JUDGE_START_INDEX": str(self.llm_judge_start_index),
                "LLM_JUDGE_END_INDEX": str(self.llm_judge_end_index),
            }
        )
        return base_env


def run_script(script_dir: str, file_name: str, env: dict, stop_on_error: bool) -> bool:
    script_path = os.path.join(script_dir, "main_code", file_name)
    if not os.path.exists(script_path):
        print(f"找不到脚本: {script_path}")
        return False
    print(f"\n========== 开始执行: {file_name} ==========")
    completed = subprocess.run([sys.executable, script_path], cwd=script_dir, env=env)
    if completed.returncode != 0:
        print(f"执行失败: {file_name} (exit_code={completed.returncode})")
        if stop_on_error:
            return False
    print(f"========== 执行结束: {file_name} ==========")
    return True


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(script_dir, ".env"))
    cfg = WorkflowConfig()
    os.makedirs(os.path.join(script_dir, cfg.dataset_name), exist_ok=True)
    env = cfg.to_env(script_dir)

    required_keys = ["API_KEY", "OPENROUTER_KEY"]
    missing = [k for k in required_keys if not (env.get(k) or "").strip()]
    if missing:
        print(f"缺少必要环境变量: {missing}")
        print("请先在 .env 或系统环境中设置后再运行。")
        sys.exit(1)

    stages = [
        "get_surveys_deepresearch.py",
        "check_paper_inclusion.py",
        "solve_question_with_survey.py",
        "check_percentage_exit_or_not.py",
        "llm_judge.py",
    ]

    for stage in stages:
        ok = run_script(script_dir, stage, env, cfg.stop_on_error)
        if not ok:
            sys.exit(1)

    print("\n工作流执行完成。")


if __name__ == "__main__":
    main()
