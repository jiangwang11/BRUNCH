# BRUNCH

This project provides an automated pipeline to benchmark Large Language Models (LLMs) on their ability to generate academic surveys, answer specific research questions based on those surveys, and accurately recall papers. 

The pipeline is highly configurable, supporting different models for problem generation, filtering, field extraction, survey generation, and evaluation. It integrates seamlessly with OpenAI-compatible APIs (like OpenRouter or AiHubMix).

## 📂 Project Structure

```text
script/
├── data/
│   ├── papers.csv
│   └── ... 
├── src/
│   ├── get_problem.py
│   ├── filter.py
│   └── ...
├── output/       
|   ├── openai_batch_output.filtered.json
│   └── ... 
├── .env
├── workflow_main.py
└── workflow_without_question_generation.py
```

## 🚀 Setup & Installation

1. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install openai python-dotenv httpx numpy jieba
   ```

2. **Configure API Keys**:
   Create a `.env` file in the `script/` directory and add your API keys:
   ```env
   OPENROUTER_KEY=sk-or-v1-...
   API_KEY=sk-or-v1-...
   ```
   *(Note: The workflow will automatically map `API_KEY` to `OPENROUTER_KEY` if one is missing).*

## 🛠️ How to Run the Workflows

The project provides two main workflow scripts. You can easily configure the models, dataset paths, and batch sizes directly within the `WorkflowConfig` dataclass inside these files.

### 1. Full End-to-End Workflow
This script runs the entire pipeline from scratch: reading the CSV, generating questions, filtering them, extracting fields, generating surveys, and finally evaluating the results.

```bash
cd script/
python workflow_main.py
```

**Key Configurations in `workflow_main.py`**:
```python
@dataclass
class WorkflowConfig:
    student_model: str = "qwen/qwen3-8b"              # Model used to answer questions during filtering & evaluation
    problem_generation_model: str = "openai/gpt-4o-mini" # Model used to generate initial questions
    teacher_model: str = "qwen/qwen3-8b"              # Model used for final LLM judging
    dataset_name: str = "test_workflow"               # Output folder name inside `output/`
    paper_csv_path: str = "data/papers.csv"           # Input dataset
    num_to_process: int = 4                           # Number of papers to process
    survey_model: str = "qwen/qwen3-8b"               # Model used to write the survey
    field_model: str = "openai/gpt-5-mini"            # Model used to extract research fields
```

### 2. Workflow (Skipping Question Generation)
If you already have pre-generated questions (`openai_batch_output.filtered.json`) and fields (`paper_fields_output.json`) placed in the `output/` directory, you can run this script to skip the expensive generation/filtering steps and go straight to survey generation and evaluation.

```bash
cd script/
python workflow_without_question_generation.py
```

## 📊 Outputs & Evaluation

All generated files are safely stored in the `output/<dataset_name>/` directory.
- **Surveys**: Markdown files are saved in model-specific subdirectories (e.g., `output/test_workflow/qwen_qwen3-8b/01_Survey_...md`). This prevents different models from overwriting each other's results.
- **`survey_check_result_*.json`**: Contains the evaluation of whether the target paper was successfully included in the survey.
- **`survey_direct_compare_result_*.json`**: Contains the results of the model attempting to answer the generated questions using *only* the generated survey.
- **`final_result_*.json`**: The final comprehensive scores evaluated by the `llm_judge.py`.

## ⚙️ Customization

### Changing the API Base URL
To change the API Base URL (e.g., from OpenRouter to a custom proxy or local server), you can modify the base URL environment variables mapped inside the `to_env` method of the workflow scripts:
```python
"SOLVE_API_BASE_URL": "https://openrouter.ai/api/v1"
```

### Using Your Own Custom Model on a Private Server for Survey Generation

If you have deployed your own Large Language Model (e.g., via vLLM, Ollama, or FastChat) on a private server and want to use it specifically to generate surveys, you can do so by making a few adjustments. This setup assumes your custom server provides an OpenAI-compatible API endpoint.

1. **Deploy Your Model**:
   Ensure your model is running and accessible. For example, if you deploy using vLLM on your server (`http://your-server-ip:8000`), the OpenAI-compatible endpoint would typically be `http://your-server-ip:8000/v1`.

2. **Update Workflow Configuration**:
   Open `workflow_main.py` (or `workflow_without_question_generation.py`) and modify the `to_env` method to point the `SURVEY_API_BASE_URL` to your server.
   
   Locate the `base_env.update({ ... })` block and add or modify the base URL specific to the survey generation script:
   
   ```python
   # In workflow_main.py or workflow_without_question_generation.py
   base_env.update(
       {
           # ... other variables ...
           "SURVEY_MODEL": "your-custom-model-name", # The name you defined when deploying
           "SURVEY_HEALTH_CHECK_MODEL": "your-custom-model-name",
           "SURVEY_API_BASE_URL": "http://your-server-ip:8000/v1", # Your private server endpoint
           # ... other variables ...
       }
   )
   ```

3. **Modify `get_surveys_deepresearch.py` (if necessary)**:
   The `get_surveys_deepresearch.py` script already reads `SURVEY_API_BASE_URL` from the environment. Ensure it defaults correctly or reads it explicitly:
   
   ```python
   # In src/get_surveys_deepresearch.py
   OPENROUTER_BASE_URL = os.environ.get("SURVEY_API_BASE_URL", "https://openrouter.ai/api/v1")
   ```
   *Note: Despite the variable name `OPENROUTER_BASE_URL`, the script uses the value provided by `SURVEY_API_BASE_URL` in the environment.*

4. **API Key Considerations**:
   If your local/private deployment does not require an API key (e.g., local vLLM instance without auth), you can pass a dummy key in your `.env` file because the OpenAI Python client usually requires *some* string to initialize:
   ```env
   OPENROUTER_KEY=dummy-key-for-local-server
   ```
   If your server does require authentication, provide the correct key here.

By following these steps, the survey generation stage (`get_surveys_deepresearch.py`) will route its requests to your private server, while other stages can independently use OpenRouter or AiHubMix as configured.
