# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from fastapi import FastAPI
from generate_voice import generate_audio
import requests
from elevenlabs import set_api_key


app = FastAPI()


@app.get("/voice")
async def get_voice():
    audio = generate_audio()
    url = "https://api.elevenlabs.io/v1/voices/add"
    headers = {"x-api-key": "55ce16928997e63887ab6a150c7cbe39"}
    payload = {
        "files": [audio],
        "name": "Rachel D"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print("Response text from eleven labs voice api - " + response.text)
    return {"voice": response.text}
