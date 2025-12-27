from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.saveFile import save_base64_image_cv2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class ImageData(BaseModel):
    image_data: str


@app.post("/img_predit")
def run_image_inference(base64_img: ImageData):
    image_path = save_base64_image_cv2(base64_img)

    try:

        result = "model_output"
        return result
    finally:
        if image_path.exists():
            image_path.unlink()
