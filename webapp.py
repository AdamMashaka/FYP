import cv2
from ultralytics import YOLO
import pyttsx3

# Initialize the YOLO model
model = YOLO('yolov9c.pt')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Capture video from the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform the detection
    results = model(frame)
    
    # Draw bounding boxes on the frame
    frame = results[0].plot()

    # Get the detected objects
    detections = results[0].boxes.data.cpu().numpy()  # Convert detections to numpy array
    for det in detections:
        class_id = int(det[5])
        class_name = model.names[class_id]
        
        # Announce the detected object
        engine.say(f'{class_name} is detected')
        engine.runAndWait()

    # Display the frame with detections
    cv2.imshow('Object Detection', frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
