from click import prompt
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) #Input your API key here


def get_agro_advice(crop_name):
    prompt = f"""
You are an expert in Nigerian agriculture, crop processing, and market advisory.

A user entered: "{crop_name}"

First: Decide if this is a real **farm produce** (e.g., cassava, maize, tomato, catfish). 
If it's not valid (like "laptop" or "aeroplane"), respond:
"❌ '{crop_name}' is not a valid farm produce. Please enter something like maize, cassava, yam, or tomatoes."

If it's valid, give detailed advice in numbering points:
 1. *Best time to plant {crop_name} according to Nigeria weather*:
    - [Answer]

    2. *Best time to harvest {crop_name} according to Nigeria weather*:
    - [Answer]

    3. *Best time to sell {crop_name} according to Nigeria weather*:
    - [Answer]

    4. *Best region to plant {crop_name} in Nigeria*:
    - [Answer]

    5. *How to process it into value-added products*:
    - [Answer]

    6. *Storage tips (short-term and long-term)*:
    - [Answer]

    7. *Packaging advice*:
    - [Answer]

    8. *Suggested platforms or locations to sell*:
    - [Answer]

    9. *A catchy Nigerian business name for the product*:
    - [Answer]
"""

    model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
    response = model.generate_content(prompt.replace("[Crop]", crop_name))
    return response.text

