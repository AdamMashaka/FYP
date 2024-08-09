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


```
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

sleep 20  # Wait for 20 seconds to ensure all services are up
/usr/bin/python3 /home/project-houston/Downloads/object_detection/install_and_r>

exit 0

``` mport subprocess
import sys

# List of packages to install
packages = ['opencv-python', 'numpy', 'pyttsx3']

# Install each package if not already installed
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Now run your main script
subprocess.run([sys.executable, "/home/Downloads/object_detection/tensor.py">








                              [ Read 12 lines ]
^G Help        ^O Write Out   ^W Where Is    ^K Cut         ^T Execute
^X Exit        ^R Read File   ^\ Replace     ^U Paste       ^J Justify

```



```
import subprocess
import sys

# List of packages to install
packages = ['opencv-python', 'numpy', 'pyttsx3']

# Install each package if not already installed
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Now run your main script
subprocess.run([sys.executable, "/home/Downloads/object_detection/tensor.py">




```


bgs

```
project-houston@AI:~/Downloads/object_detection $ /usr/bin/python3 /home/project-houston/Downloads/object_detection/install_and_run.py
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: opencv-python in /home/project-houston/.local/lib/python3.9/site-packages (4.10.0.84)
Requirement already satisfied: numpy>=1.19.3 in /home/project-houston/.local/lib/python3.9/site-packages (from opencv-python) (1.26.4)

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: python3 -m pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: numpy in /home/project-houston/.local/lib/python3.9/site-packages (1.26.4)

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: python3 -m pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: pyttsx3 in /home/project-houston/.local/lib/python3.9/site-packages (2.90)

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: python3 -m pip install --upgrade pip
Traceback (most recent call last):
  File "/home/project-houston/Downloads/object_detection/tensor.py", line 51, in <module>
    cv2.imshow('Object Detection', frame)
cv2.error: OpenCV(4.10.0) /io/opencv/modules/highgui/src/window.cpp:1301: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'

project-houston@AI:~/Downloads/object_detection $ 

```
