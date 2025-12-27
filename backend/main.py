from fastapi import FastAPI, HTTPException
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


@app.post("/img_predict")
def run_image_inference(base64_img: ImageData):
    image_path = None

    try:
        # Access request data correctly
        image_path = save_base64_image_cv2(base64_img.image_data)

        # TODO: run your ML model here
        result = "model_output"

        return {
            "success": True,
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Clean up saved image
        if image_path and image_path.exists():
            image_path.unlink()
