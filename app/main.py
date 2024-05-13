import os

import numpy as np
import torch
import uvicorn
from mobile_sam import SamAutomaticMaskGenerator, SamPredictor, sam_model_registry
from PIL import Image

from app.tools import box_prompt, format_results, point_prompt, fast_process

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
import imghdr

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

sam_checkpoint = "./mobile_sam.pt"
model_type = "vit_t"

mobile_sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
mobile_sam = mobile_sam.to(device=device)
mobile_sam.eval()

mask_generator = SamAutomaticMaskGenerator(mobile_sam)
predictor = SamPredictor(mobile_sam)

app = FastAPI()

@torch.no_grad()
def segment_everything(
    image,
    input_size=1024,
    better_quality=False,
    withContours=True,
    use_retina=True,
    mask_random_color=True,
):
    global mask_generator

    input_size = int(input_size)
    w, h = image.size
    scale = input_size / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = image.resize((new_w, new_h))

    nd_image = np.array(image)
    annotations = mask_generator.generate(nd_image)

    fig = fast_process(
        annotations=annotations,
        image=image,
        device=device,
        scale=(1024 // input_size),
        better_quality=better_quality,
        mask_random_color=mask_random_color,
        bbox=None,
        use_retina=use_retina,
        withContours=withContours,
    )
    return fig

def is_image(file):
    image_format = imghdr.what(None, h=file.read())
    return image_format is not None

@app.post("/segment-image")
async def segment_image(file: UploadFile= File(...)):
    if not is_image(file.file):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")
    file.file.seek(0)
    contents = await file.read()
    try:
        image = Image.open(BytesIO(contents)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")
    segment_everything_result = segment_everything(image=image)
    buffered = BytesIO()
    segment_everything_result.save(buffered, format="PNG")
    buffered.seek(0)
    return StreamingResponse(buffered, media_type="image/png")
    
