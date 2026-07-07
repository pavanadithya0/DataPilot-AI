import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError, ServerError

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_gemini(prompt: str) -> str:
    retries = 3

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text.strip()

        except ServerError:
            if attempt < retries - 1:
                time.sleep(5)
                continue
            raise

        except ClientError as e:
            # Handle temporary rate limit
            if "RESOURCE_EXHAUSTED" in str(e):
                if attempt < retries - 1:
                    time.sleep(20)
                    continue

                raise Exception(
                    "Gemini API quota exceeded. Please wait a while or use another API key."
                )

            raise