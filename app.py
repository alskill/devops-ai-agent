from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

print("=" * 60)
print("🤖 DevOps AI Agent")
print("=" * 60)

question = input("Ask your DevOps AI Agent: ")

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question
    )

    print("\n🤖 AI Response:\n")
    print(response.text)

except Exception as e:
    print("\n❌ Error:", e)
    print("\nPlease try again in a few moments.")