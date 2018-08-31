# MVAV

## Setting up your environment
**Pre requisites**
* Python3
* pip3  
* OpenCV
```sh
sudo apt update
sudo apt install python3-pip
sudo apt install python3-opencv
sudo -H pip3 install bpython
```

**Pull the github repo**
```sh
git clone git clone https://github.com/sturzl/mvav.git
```
**Test your setup**
Run
```sh
python3 setup_test.py
```
Which is a script that runs the following python. It should display an image of a mock track, and print to the command line.
```python
import cv2 as cv
image = cv.imread('images/tapered_nobackground.jpg')
cv.imshow('image',image)
cv.waitKey(0)
cv.destroyAllWindows()
print('Great Success!')
```

## Reading images from the raspi

* Google for reading images from an ip cam
* Needs to be a jpeg stream? or .mjpg for the easiest version
* check out [this code sample](https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv) that uses OpenCV  
  ```python
  cap = cv2.VideoCapture("http://192.168.18.37:8090/test.mjpeg")```
