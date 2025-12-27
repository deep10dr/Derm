import base64
import uuid
from pathlib import Path

import cv2
import numpy as np

TEMP_IMAGE_DIR = Path("./temp/images").resolve()


def base64_to_cv2_image(base64_str: str) -> np.ndarray:
    """
    Convert base64 string to OpenCV image (numpy array)
    """
    # Remove data URL header if present
    if "," in base64_str:
        base64_str = base64_str.split(",")[1]

    try:
        img_bytes = base64.b64decode(base64_str)
    except Exception:
        raise ValueError("Invalid base64 image")

    img_array = np.frombuffer(img_bytes, dtype=np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError("Could not decode image")

    return image


def save_base64_image_cv2(base64_str: str) -> Path:
    """
    Save base64 image as temp file using OpenCV
    """
    image = base64_to_cv2_image(base64_str)

    TEMP_IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"img_{uuid.uuid4().hex}.png"
    file_path = TEMP_IMAGE_DIR / filename

    success = cv2.imwrite(str(file_path), image)
    if not success:
        raise RuntimeError("Failed to write image to disk")

    return file_path
