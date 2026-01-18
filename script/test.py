import openai

client = openai.OpenAI(
  api_key="sk-DdCFk4gxi3szmjHK28339049E1954437Bd19B1E3D0790b06",  # 换成你在 AiHubMix 生成的密钥
  base_url="https://aihubmix.com/v1"
)

response = client.embeddings.create(
  input="Your text string goes here",
  model="text-embedding-3-small"
)

print(response.data[0].embedding)