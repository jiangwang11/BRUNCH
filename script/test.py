import openai

client = openai.OpenAI(
  api_key="sk-DdCFk4gxi3szmjHK28339049E1954437Bd19B1E3D0790b06",  # Replace with your AIHubMix generated key
  base_url="https://aihubmix.com/v1"
)

response = client.chat.completions.create(
  model="gemma-3-27b-it",
  messages=[
      {"role": "user", "content": "Hello, how are you?"}
  ]
)

print(response.choices[0].message.content)