import os
import shutil
import numpy as np
import pandas as pd
from PIL import Image
import torch
from facenet_pytorch import MTCNN
import dlib
import streamlit as st
import matplotlib.pyplot as plt
import logging
logging.getLogger('streamlit').setLevel(logging.ERROR)

# your own dlib helpers
from my_dlib_funcs import get_descriptors, recognize, display

# -------------------------------------------------------------------
# UI HEADER
# -------------------------------------------------------------------
st.title("🎥🍿InScene_Ver1: A lightweight FR pipeline for in-scene 🎞️ actor recognition 🤔")

# -------------------------------------------------------------------
# UTILS
# -------------------------------------------------------------------
def empty_folder(folder_path: str):
    """Delete every file inside a folder."""
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# -------------------------------------------------------------------
# INIT MODELS
# -------------------------------------------------------------------
device = torch.device("cpu")          # change to "cuda" if GPU + facenet_pytorch compiled
mtcnn = MTCNN(keep_all=True, device=device)

output_folder = "cropped_queries"
os.makedirs(output_folder, exist_ok=True)

cnn_model_path = "models/mmod_human_face_detector.dat"
shape_predictor_path = "models/shape_predictor_68_face_landmarks_GTX.dat"
face_recognition_model_path = "models/dlib_face_recognition_resnet_model_v1.dat"

dlib.DLIB_USE_CUDA = True
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_model_path)
predictor = dlib.shape_predictor(shape_predictor_path)
face_rec = dlib.face_recognition_model_v1(face_recognition_model_path)

# -------------------------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------------------------
uploaded_file = st.file_uploader("Upload a scene frame", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read as PIL
    img = Image.open(uploaded_file).convert("RGB")

    # Show the original
    st.image(img, caption="Uploaded Frame", use_container_width=True)

    # Detect faces
    boxes, _ = mtcnn.detect(img)

    # ----------------------------------------------------------------
    # SAVE CROPS
    # ----------------------------------------------------------------
    crop_paths = []
    if boxes is not None:
        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = [int(b) for b in box]
            cropped_face = img.crop((x1, y1, x2, y2))

            # enforce clean filename + extension
            base = os.path.splitext(uploaded_file.name)[0]
            cropped_filename = f"crop_{i}_{base}.jpg"
            cropped_path = os.path.join(output_folder, cropped_filename)
            cropped_face.save(cropped_path, format="JPEG")
            crop_paths.append(cropped_path)

        #st.success(f"{len(crop_paths)} faces cropped and saved.")
        #st.image([Image.open(p) for p in crop_paths], caption=[os.path.basename(p) for p in crop_paths])
    else:
        st.warning("No faces detected!")

    # ----------------------------------------------------------------
    # FACE RECOGNITION (if any faces cropped)
    # ----------------------------------------------------------------
    if boxes is not None and len(boxes) > 0:
        try:
            # load gallery embeddings
            gallery_df = pd.read_pickle("gallery_embeddings.pkl")
            gallery_descriptors = gallery_df.to_dict(orient="records")

            # convert numpy to dlib.vector
            for row in gallery_descriptors:
                row["face descriptor"] = dlib.vector(row["face descriptor"])

            # run query
            query_descriptors = get_descriptors(
                imgs_path=output_folder,
                face_detector=cnn_face_detector,
                shape_predictor=predictor,
                face_recognizer=face_rec
            )
            recognize(gallery_descriptors, query_descriptors)

            # render results
            fig = display(query_descriptors, save_output=False)  # your my_dlib_funcs should return matplotlib fig
            #st.pyplot(fig)
            old_pyplot = st.pyplot
            def quiet_pyplot(*args, **kwargs,):
                if not args:      # no figure passed
                    fig = plt.gcf()
                    return old_pyplot(fig, **kwargs)
                return old_pyplot(*args, **kwargs)

            st.pyplot = quiet_pyplot
            st.pyplot(fig)



        except FileNotFoundError as e:
            st.error(f"Gallery pickle not found: {e}")

        # clean up after each run
        empty_folder(output_folder)

