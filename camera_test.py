import cv2

cap = cv2.VideoCapture(0)  # try 0, if not working change to 1 or 2
if not cap.isOpened():
    raise RuntimeError("Webcam not found. Try index 1 or 2.")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    cv2.imshow("Camera Test - Press ESC to quit", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
