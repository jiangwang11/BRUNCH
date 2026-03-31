import json
import os
import requests

def main():
    print("Starting script...")
    
    # ConfigurationD:\GitHub\DeepResearch_Survey_benchmark\script\survey\x-ai_grok-deep_research
    survey_dir = r"d:\GitHub\DeepResearch_Survey_benchmark\script\survey\x-ai_grok-deep_research"
    json_path = r"d:\GitHub\DeepResearch_Survey_benchmark\script\openai_batch_output.filtered.json"
    output_path = "context.json"
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        print("Please set the OPENROUTER_API_KEY environment variable.")
        return

    # Load JSON data once
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Read JSON data: {len(data)} items")
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return

    # Get list of survey files
    try:
        survey_files = os.listdir(survey_dir)
    except Exception as e:
        print(f"Error reading survey directory: {e}")
        return

    # Process IDs 1 to 25
    for target_id in range(1, 26):
        print(f"\nProcessing ID: {target_id}")
        
        # Check if already processed
        existing_data = {}
        if os.path.exists(output_path):
            try:
                with open(output_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
            except Exception as e:
                print(f"Error reading existing context.json: {e}")

        # Find the survey file starting with the ID
        survey_filename = next((f for f in survey_files if f.startswith(f"{target_id}_") or f.startswith(f"{target_id:02d}_")), None)
        
        if not survey_filename:
            print(f"Survey file for ID {target_id} not found. Skipping.")
            continue

        survey_id = survey_filename.split("_")[0] # Should match target_id roughly
        
        # Check if already processed by survey_id or target_id (as string)
        if survey_id in existing_data or str(target_id) in existing_data:
            print(f"ID {target_id} (survey_id: {survey_id}) already processed. Skipping.")
            continue
            
        survey_path = os.path.join(survey_dir, survey_filename)

        # 1. Read the survey file
        try:
            with open(survey_path, "r", encoding="utf-8") as f:
                survey_content = f.read()
            print(f"Read survey file: {survey_filename} ({len(survey_content)} chars)")
        except Exception as e:
            print(f"Error reading survey file {survey_filename}: {e}")
            continue

        # 2. Find the question
        question_item = next((item for item in data if item.get("id") == target_id), None)
        
        if question_item:
            question_text = question_item.get("question", "")
        else:
            print(f"Question with id {target_id} not found in JSON. Skipping.")
            continue

        # 3. Call OpenRouter API
        prompt = f"""
你是一个student model。请基于survey回答问题。
输出内容包括：
1. 你从survey中学到的与该题相关的关键信息；
2. 你引用的survey中的一句关键证据；
3. 简洁的推理摘要；
4. 最终答案。
不要输出冗长的内部思维链。

Context (Survey):
{survey_content}

Question:
{question_text}

Output Format (JSON):
{{
  "survey_learning_process": "...",
  "evidence_quote": "...",
  "reasoning_summary": "...",
  "answer": "..."
}}
Ensure the output is valid JSON.
"""

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "qwen/qwen-2.5-72b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"} 
        }

        print(f"Calling API for ID {target_id}...")
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            
            # Extract the content
            content = result["choices"][0]["message"]["content"]
            
            # Parse the content as JSON
            try:
                parsed_content = json.loads(content)
            except json.JSONDecodeError:
                print(f"Model response for ID {target_id} was not valid JSON, saving raw content.")
                parsed_content = {"raw_content": content}

            # 4. Write to context.json (Update incrementally)
            # Read existing context.json to append/update
            existing_data = {}
            if os.path.exists(output_path):
                try:
                    with open(output_path, "r", encoding="utf-8") as f:
                        existing_data = json.load(f)
                except Exception as e:
                    print(f"Error reading existing context.json: {e}")
            
            # Handle legacy flat format
            if "answer" in existing_data and "01" not in existing_data:
                existing_data = {"01": existing_data}
                
            # Add the new result
            existing_data[survey_id] = parsed_content

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, ensure_ascii=False, indent=4)
                
            print(f"Successfully wrote response for ID {target_id} to {output_path}")

        except Exception as e:
            print(f"Error calling API for ID {target_id}: {e}")
            if 'response' in locals():
                print(f"Response text: {response.text}")

if __name__ == "__main__":
    main()
