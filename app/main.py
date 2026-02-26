import os
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Telugu Movie Generator")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
# )

@app.get("/random-telugu-movie")
def get_random_telugu_movie():
    prompt = "Give me only one random popular Telugu movie name with atmost ten(10) letters only. Only the movie name. No explanation."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1.2  # Higher temperature for randomness
    )

    movie_name = response.choices[0].message.content.strip()

    return {
        "movie": movie_name
    }