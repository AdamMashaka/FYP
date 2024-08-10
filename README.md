# Project Name: Blind Assistor stick

## Project Description
Blind stick is the FYP project that deal with connecting of Robotics and AI/ML that will help blind man to know what it is ahead of him or she.

**Team Members:**
- Adam .M. Katani
- Github: @AdamMAshaka 
-Email: mashakaadam123@gmail.com

-Ramadan Kidola
-Github: @dollatron
-Email:     

-Engineer Brian
-Github:
-Email: 

kind of flow chart we will use is 


<img src="ai.png" alt="drawing" width="400" height="200"/>


## Technologies Used

- Python for intergration of Web camera and Object.
- pytorch: For clear of object seen.
- pyttsx 
- yolov9 


```sh
   pip install opencv-python opencv-python-headless

```

```sh
wget https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/deploy.prototxt
wget https://github.com/chuanqi305/MobileNet-SSD/raw/master/mobilenet_iter_73000.caffemodel
   
```   




## How It Works

1. User open the application
2. User run the server
3. User show the object
4. Adam will tell you what it is.

## Showcase Video

[Watch the Showcase Video](https://Github.com/AdamMashaka)

## Submission Details

**Repository:** [GitHub Repository](https://github.com/AdamMashaka/bliind_DIT)
**Demo:** [Live Demo](https://)

# You wanna fork it? 
  just fork it and push you are changes in my origin directory  

  ```sh
     git fetch origin
     git merge origin/main
     # Resolve any merge conflicts if necessary
     git add <resolved-file>  # Only if there were conflicts
     git commit -m "Resolve merge conflicts"  # Only if there were conflicts
     git push origin main

```


## How you are pi should lopojk like
```
!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

python3 /home/pi/Downloads/object_detection/tensor.py &
                               [ Read 24 lines ]
^G Help      ^O Write Out ^W Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^_ Go To Line


```
## install_and_run.py 
```
import subprocess
import sys

# List of packages to install
packages = ['opencv-python', 'numpy', 'pyttsx3']

# Install each package if not already installed
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Now run your main script
subprocess.run([sys.executable, "/home/Downloads/object_detection/tensor.py"])
```


## Do not forget t add this in you are Rasberry pi local to run by automatic  

```
  sleep 20
source /home/pi/.bashrc
source /home/pi/your_env/bin/activate
python3 /home/pi/Downloads/object_detection/tensor.py &

```

## Do not forget to give it a star

##  GIVE CREDIT TO ADAM KATANI

## this is modified tensor.py after to detect object will tell which direction it is 

```
import cv2
import numpy as np
import pyttsx3
import threading

# Load the MobileNet SSD model
net = cv2.dnn.readNetFromCaffe('/home/project-houston/Downloads/object_detection/deploy.prototxt', '/home/project-houston/Downloads/object_detection/mobilenet_iter_73000.caffemodel')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Class labels MobileNet SSD was trained on
classNames = {0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
              5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair', 10: 'cow',
              11: 'diningtable', 12: 'dog', 13: 'horse', 14: 'motorbike', 15: 'person',
              16: 'pottedplant', 17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}

# Capture video from the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

def announce(label, position):
    engine.say(f'{label} is detected on the {position}')
    engine.runAndWait()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get the center of the frame
    frame_center = frame.shape[1] // 2

    # Prepare the frame for object detection
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")

            label = classNames[idx]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Determine if the object is on the left or right side of the frame
            if startX < frame_center:
                position = "left"
            else:
                position = "right"

            # Announce the detected object and its position in a separate thread
            threading.Thread(target=announce, args=(label, position)).start()

    # Display the frame with detections
    cv2.imshow('Object Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
```
