import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit UI
st.title("Image Segmentation App")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Segment Image"):
        # Uploading the image to FastAPI
        files = {'file': uploaded_file.getvalue()}
        response = requests.post('http://localhost:8000/segment-image', files=files)

        if response.status_code == 200:
            # Gettting the segmented image
            segmented_image_bytes = response.content
            segmented_image = Image.open(BytesIO(segmented_image_bytes))

            # Displaying segmented image
            st.image(segmented_image, caption="Segmented Image", use_column_width=True)
        else:
            st.error("Error occurred while segmenting image.")
