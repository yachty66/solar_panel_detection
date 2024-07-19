from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/upload-image/")
async def upload_image(request):
    print(request)
    # Simply return the received encoded image
    return JSONResponse(content={"encoded_image": request.encoded_image})