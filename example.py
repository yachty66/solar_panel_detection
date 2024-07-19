import requests
import base64

# Replace with the actual URL of your deployed FastAPI app
url = "https://your-heroku-app.herokuapp.com/upload-image/"

# Read an image file and encode it in base64
with open("1.jpeg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the payload
payload = {
    "encoded_image": encoded_image
}

# Send a POST request to the FastAPI endpoint
response = requests.post(url, json=payload)

# Print the response from the server
print(response.json())