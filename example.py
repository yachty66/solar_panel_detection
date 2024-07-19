import requests
import base64

# Replace with the actual URL of your deployed FastAPI app
url = " https://stark-forest-83066-3497ed276c90.herokuapp.com/endpoint"

# Read an image file and encode it in base64
with open("5.jpeg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the payload
payload = {
    "encoded_image": encoded_image
}

# Send a POST request to the FastAPI endpoint
response = requests.post(url, json=payload)

# Print the response from the server
print(response.text)