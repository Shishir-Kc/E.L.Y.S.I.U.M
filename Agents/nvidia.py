from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = ""
)

response = client.responses.create(
    model="nvidia/nemotron-3-ultra-550b-a55b",
    input="hello !"
)

print(response.output_text)

