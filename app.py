from google import genai
from config import GEMINI_API_KEY
import time

client = genai.Client(api_key=GEMINI_API_KEY)

print("=" * 60)
print("🤖 DevOps AI Agent")
print("=" * 60)

while True:
    question = input("\nAsk your DevOps AI Agent (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=question
        )

        print("\n🤖 AI Response:\n")
        print(response.text)

    except Exception as e:
        print("\nError:", e)
        print("Waiting 60 seconds before allowing another request...")
        time.sleep(60)