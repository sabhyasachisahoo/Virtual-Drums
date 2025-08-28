import cv2
import mediapipe as mp
import pygame
import math
import time
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller exe """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Init pygame mixer
pygame.mixer.init()

# Load sounds
kick   = pygame.mixer.Sound(resource_path("sounds/kick.wav"))
snare  = pygame.mixer.Sound(resource_path("sounds/snare.wav"))
hihat  = pygame.mixer.Sound(resource_path("sounds/hihat.wav"))

# Mediapipe setup
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

# Drum pad positions
drum_points = {
    "kick": (150, 300),
    "snare": (350, 300),
    "hihat": (550, 300),
}
drum_sounds = {"kick": kick, "snare": snare, "hihat": hihat}
hit_radius = 60

# Track hits per hand
hand_hits = {}   # {hand_id: {drum: inside?}}
flash_time = {name: 0 for name in drum_points}

with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=2
) as hands:

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        h, w, _ = frame.shape

        if results.multi_hand_landmarks:
            for i, hand in enumerate(results.multi_hand_landmarks):
                hand_id = i

                # Init memory for this hand
                if hand_id not in hand_hits:
                    hand_hits[hand_id] = {name: False for name in drum_points}

                # Track fingertip (index finger tip = landmark 8)
                x = int(hand.landmark[8].x * w)
                y = int(hand.landmark[8].y * h)
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

                # Check each drum
                for name, (cx, cy) in drum_points.items():
                    dist = math.hypot(x - cx, y - cy)
                    inside = dist < hit_radius

                    if inside and not hand_hits[hand_id][name]:
                        drum_sounds[name].play()
                        flash_time[name] = time.time()

                    hand_hits[hand_id][name] = inside

        # Draw drums
        for name, (cx, cy) in drum_points.items():
            if time.time() - flash_time[name] < 0.2:
                color, thickness = (0, 0, 255), -1
            else:
                color, thickness = (255, 0, 0), 2
            cv2.circle(frame, (cx, cy), hit_radius, color, thickness)
            cv2.putText(frame, name, (cx - 30, cy - 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Virtual Drums", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

cap.release()
cv2.destroyAllWindows()
