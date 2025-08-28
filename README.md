# 🥁 Virtual Drums

Play drums in the air using your hands and your webcam!  
This project uses **Python**, **Pygame**, and **Mediapipe** to track your hands and trigger drum sounds in real time.

---

## ✨ Features
- Hand-tracking using [Mediapipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker).
- Virtual drum kit (kick, snare, hihat).
- Real-time sound playback with Pygame.
- Can be packaged into a standalone `.exe` with PyInstaller.

---

## 📦 Requirements
- Python 3.10+
- [Pygame](https://www.pygame.org/)
- [Mediapipe](https://pypi.org/project/mediapipe/)
- OpenCV (`cv2`)

▶️ Usage

1. Clone the repo:
'''
git clone https://github.com/your-username/virtual-drums.git
cd virtual-drums

2.Run the script:
'''
python virtual_drums.py
'''
3. Move your hands in front of the webcam to play drums:
'''
Left hand = kick
Right hand = snare
Other gestures = hihat
'''
