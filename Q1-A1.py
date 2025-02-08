import cv2
import os

# Creates a folder to store images
save_dir = "snapshots"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to get the next image filename
def get_next_filename():
    count = 1
    while os.path.exists(os.path.join(save_dir, f"image{count}.jpg")):
        count += 1
    return os.path.join(save_dir, f"image{count}.jpg")

cap = cv2.VideoCapture(0)  # (0) Opens the default camera (I Changed the camera to 1 as I used an external camera and then reverted it back to 0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow("Photo Booth - Press 's' to take a snapshot", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Press 's' to save the snapshot
        filename = get_next_filename()
        cv2.imwrite(filename, frame)
        print(f"Snapshot saved: {filename}")

    elif key == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()