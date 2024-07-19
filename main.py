from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/upload-image/")
async def upload_image(request: Request):
    body = await request.json()
    encoded_image = body.get("encoded_image")
    return JSONResponse(content={"encoded_image": encoded_image})