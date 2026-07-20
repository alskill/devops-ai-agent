from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

question = input("Ask your DevOps AI Agent: ")

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=question
)

print("\n🤖 AI Response:\n")
print(response.text)
print(response.text)