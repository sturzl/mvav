# MVAV

**Minimum Viable Autonomous Vehicle**

## Reading images from raspi
* Needs to be a jpeg stream? or .mjpg for the easiest version

## Reading images into opencv/simple cv

* Google for reading images from an ip cam
* check out [this code sample](https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv) that uses OpenCV  
  ```python
  cap = cv2.VideoCapture("http://192.168.18.37:8090/test.mjpeg")
  ```
## Script for finding the red line from a static image
**Pre requisites**
* Python3
* pip3  
* OpenCV
  ```sh
  sudo apt install python3-pip
  sudo -H pip3 install opencv-python
  sudo -H pip3 install bpython
  ```
**The script**
```python
import cv2 as cv
image = cv.imread('tapered_nobackground.jpg')
cv.imshow('image',image)
cv.waitKey(0)
cv.destroyAllWindows()
```

