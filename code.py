from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="APIM Gateway URL",
    api_key="APIM subscription key",
    api_version="2023-12-01-preview",
)
response = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[{"role": "system", "content": "You are a scientist"}, {"role": "user", "content": "What is life"}],
)
print(response)
