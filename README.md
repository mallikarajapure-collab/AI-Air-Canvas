<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:082F49,35:0891B2,70:22D3EE,100:BAE6FD&height=235&section=header&text=AI%20AIR%20CANVAS&fontSize=44&fontColor=082F49&fontAlignY=36&desc=Your%20hand.%20Your%20canvas.%20No%20touch%20needed.&descAlignY=60&descSize=15" width="100%" alt="AI Air Canvas — draw with hand gestures" />

<p><strong>Turn real-time hand movements into digital drawing using computer vision.</strong></p>

<p>
  <img src="https://img.shields.io/badge/Python-075985?style=for-the-badge&logo=python&logoColor=BAE6FD" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-0891B2?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/MediaPipe-0E7490?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe" />
  <img src="https://img.shields.io/badge/Computer%20Vision-22D3EE?style=for-the-badge&logoColor=082F49" alt="Computer vision" />
</p>

</div>

---

## 🌊 Overview

**AI Air Canvas** is a Python computer-vision project that lets you draw in the air by moving your index finger in front of a camera. OpenCV captures and displays the video, MediaPipe provides hand landmarks, and NumPy creates the drawing canvas.

The application recognises a small set of hand gestures and overlays the canvas on the live camera view. It is a hands-on exploration of gesture interaction and real-time image processing.

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🖐️ Hand tracking
- Process a live webcam feed.
- Track one hand using MediaPipe hand landmarks.
- Display detected hand landmarks and connections.

</td>
<td width="50%" valign="top">

### 🎨 Air drawing
- Draw by pointing with the index finger.
- Choose red, green, or blue drawing colours.
- Erase by switching to black.
- Clear the canvas without restarting the app.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🤘 Gesture recognition
The current gesture function recognises:
- Open palm
- Fist
- Point
- Victory
- Thumb up

Other detected poses are labelled as unknown.

</td>
<td width="50%" valign="top">

### 🖥️ Live feedback
- Display the current gesture label.
- Blend the drawing canvas with the webcam frame.
- Use keyboard shortcuts to control drawing and exit.

</td>
</tr>
</table>

## 🎮 Controls

Use the keyboard while the **AI Air Canvas** camera window is active.

| Key | Action |
|---|---|
| `R` | Select red |
| `G` | Select green |
| `B` | Select blue |
| `E` | Switch to black (erase) |
| `C` | Clear the drawing canvas |
| `Q` | Quit the application |

**Drawing gesture:** point with the index finger to draw. When the detected gesture changes away from `POINT`, the drawing stroke resets so the next stroke starts separately.

## 🧰 Tech stack

| Technology | How it is used |
|---|---|
| Python | Application logic and control flow |
| OpenCV | Webcam capture, frame processing, drawing, and display |
| MediaPipe | Hand landmark detection and hand-connection visualisation |
| NumPy | Initialise and clear the drawing canvas |

## 🔄 How it works

```text
Webcam frame
     |
     v
OpenCV captures and flips the image
     |
     v
MediaPipe detects hand landmarks
     |
     v
Gesture logic checks finger positions
     |
     v
Index-finger coordinates drive drawing
     |
     v
Canvas is blended with the live frame
     |
     v
OpenCV displays the result
```

## 🚀 Run locally

### 1. Clone the repository

```bash
git clone https://github.com/mallikarajapure-collab/AI-Air-Canvas.git
cd AI-Air-Canvas
```

### 2. Create and activate a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The requirements file lists OpenCV, MediaPipe, and NumPy.

### 4. Start the application

```bash
python app.py
```

Allow camera access if your operating system asks for it. Keep the camera window focused when using the keyboard controls.

## 📁 Project structure

```text
AI-Air-Canvas/
├── app.py
├── requirements.txt
└── .gitignore
```

## 🧪 Current scope and limitations

- Uses a local webcam; it does not connect to an external camera service.
- Processes one hand at a time with configured detection and tracking confidence thresholds.
- The current code supports red, green, blue, and black/erase modes plus clearing the canvas.
- The current implementation does **not** include a save-drawing shortcut, despite that being a possible future enhancement.
- Gesture recognition is based on simple landmark-position rules and may vary with hand orientation, lighting, and camera placement.
- The project does not use a trained custom gesture-classification model; MediaPipe supplies the hand landmarks used by the app's rule-based gesture logic.

## 🔭 Ideas for future improvements

- Add a save/export option for finished drawings.
- Introduce a colour palette and adjustable brush size.
- Improve gesture robustness across different hand orientations.
- Add a short on-screen guide for controls and camera setup.
- Include screenshots or a short demo GIF in the repository.

## 👩‍💻 Author

**Mallika Rajapure**  
MCA Student · Python, Computer Vision & Software Development

<div align="center">

**Create in the air. Bring ideas to the canvas.** 🌐

</div>
