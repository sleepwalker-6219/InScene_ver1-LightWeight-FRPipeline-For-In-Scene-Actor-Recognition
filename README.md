# 🎥🍿InScene_ver1-LightWeight-FRPipeline-For-In-Scene🎞️-Actor-Recognition🤔
This repo presents a lightweight face recognition pipeline which can be (in movies and TV shows) in the wild. This work is inspired by the **"X-Ray"** feature on **Amazon Prime video** which gives the viewer - the name and the profile of **all highlighted actors** in a scene when the **pause button** is pressed.

# Demo 👇
<video src="demo.mp4" controls width="640"></video>
[[Link to Demo]](https://youtu.be/8GYcTioPrIA "Click to watch")

# Overview of the pipeline
![Alt text](InScene_Full_Workflow_Github.png)

## 🚀 Features

* **MTCNN-based detection**: Accurate multi-scale face detection under varied lighting and pose.
* **Face alignment**: Automatic eye-based alignment for consistent embeddings.
* **Dlib embeddings**: 128D face feature vectors for robust recognition.
* **Actor recognition**: Match faces against a pre-registered set of actors.
* **Video pipeline**: Process frames from camera or video files seamlessly.
* **Modular design**: Components can be swapped (detector, embedder, classifier).

---

## 📂 Project Structure

```bash
.
├── data/                 # Store training images & samples per actor
├── models/               # Pretrained or fine-tuned models
├── src/
│   ├── detector.py       # MTCNN face detector
│   ├── aligner.py        # Face alignment utilities
│   ├── embedder.py       # Dlib embeddings wrapper
│   ├── recognizer.py     # Actor recognition logic
│   └── pipeline.py       # End-to-end pipeline script
├── notebooks/            # Jupyter notebooks for experiments
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (you are here)
└── LICENSE               # License file
```

---

## 🔧 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/in-scene-actor-recognition.git
   cd in-scene-actor-recognition
   ```

2. Set up environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download Dlib pretrained models (e.g., `shape_predictor_68_face_landmarks.dat`, `dlib_face_recognition_resnet_model_v1.dat`) and place them in the `models/` folder.

---

## 📘 Usage

### 1. Register Actors

Provide a folder with subfolders named after each actor:

```bash
data/
├── Actor_1/
│   ├── img1.jpg
│   └── img2.jpg
├── Actor_2/
│   └── img1.jpg
```

Run the embedding extraction:

```bash
python src/embedder.py --data_dir data/ --save_path models/actors_embeddings.pkl
```

### 2. Run Recognition Pipeline

Process a video file:

```bash
python src/pipeline.py --video input.mp4 --embeddings models/actors_embeddings.pkl
```

Process webcam stream:

```bash
python src/pipeline.py --camera 0 --embeddings models/actors_embeddings.pkl
```

---

## 🧪 Testing

Unit tests are provided for key components. Run them with:

```bash
pytest tests/
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* [MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/) for face detection
* [Dlib](http://dlib.net/) for face recognition embeddings
* Open-source community for continuous improvements

---

### ⭐ If you find this project helpful, don’t forget to star the repo!




