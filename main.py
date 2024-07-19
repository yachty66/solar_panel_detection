from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv
import json  # Import json to parse the response content
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)


@app.post("/endpoint")
async def upload_image(request: Request):
    # Extract the JSON body from the request
    body = await request.json()
    base64_image = body.get("encoded_image")

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are a helpful inspector with the task of detecting whether a rooftop has solar panels on top of it or not. You are given a satellite image of a rooftop, and you have to inspect the rooftop for the presence of solar panels. Also if the resolution is not clear you need to come to an decision!",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "temperature": 0.0,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    # Extract the message content from the response
    response_json = response.json()
    message_content = response_json["choices"][0]["message"]["content"]
    result = process_message_content(message_content)

    return JSONResponse(content=result)


def process_message_content(message_content):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output JSON.",
            },
            {
                "role": "user",
                "content": "Based on a response you need to decide if the text concludes that they are solar panels on a rooftop or not. you need to return true or false in the following format: {{'value': true}}. here is the response: "
                + message_content,
            },
        ],
    )
    # Parse the response content to a dictionary
    processed_content = json.loads(response.choices[0].message.content)
    return processed_content
