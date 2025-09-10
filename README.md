# 🎥🍿InScene_ver1 A LightWeight FRPipeline for In-Scene🎞️ Actor Recognition🤔
This repo presents a lightweight face recognition pipeline which can be (in movies and TV shows) in the wild. This work is inspired by the **"X-Ray"** feature on **Amazon Prime video** which gives the viewer - the name and the profile of **all highlighted actors** in a scene when the **pause button** is pressed.

# Demo 👇
<video src="demo.mp4" controls width="640"></video>
[[Link to Demo]](https://youtu.be/8GYcTioPrIA "Click to watch")

# Overview of the pipeline
![Alt text](InScene_Full_Workflow_Github.png)

## 🚀 Features

* **MTCNN-based face crop extraction**: Accurate multi-scale face extraction **In the Wild!**
* **Dlib embeddings**: **128D face feature vectors** for robust recognition.
* **Actor recognition**: Match faces against a pre-registered set of actors to output the identities of all **highlighted actors** present in a scene.
---

## 📂 Project Structure

```bash
.
├── bbt_gallery/       # Registered gallery of actors from the show - "The Big Bang Theory"
├── bbt_test/          # Some test scenes from the show - "The Big Bang Theory" to be supplied for inference.
├── office_gallery/    # Registered gallery of actors from the show - "The Office"
├── office_test/       # Some test scenes from the show - "The Office" to be supplied for inference.
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (you are here)
└── LICENSE               # License file
```

---

## 🔧 Running

Clone the repo:

   ```bash
   git clone https://github.com/yourusername/in-scene-actor-recognition.git
   cd in-scene-actor-recognition
   ```

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* [MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/) for face detection
* [Dlib](http://dlib.net/) for face recognition embeddings
  
---

### ⭐ If you find this project helpful, don’t forget to star the repo!




