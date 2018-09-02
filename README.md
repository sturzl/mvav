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

**Set up**
* Get the code
  ```sh
  git clone git clone https://github.com/sturzl/mvav.git
  ```
* Test your setup
  ```sh
  python3 setup_test.py
  ```
* You should see an image of a mock track and it should print some text. The script contains the following code:
  ```python
  import cv2 as cv
  image = cv.imread('images/straight_nobackground.jpg')
  cv.imshow('image',image)
  cv.waitKey(0)
  cv.destroyAllWindows()
  print('Great Success!')
  ```

## Generating Control Signals from images

* The general idea is to find the color for your track, then determine if you are on the track, or if the car has moved left or right. We'll use red for the target track
  * Read the image into python
  * Remove all colors except for red
  * Find the center of the red blob in the image
  * Determine how far the red blob's center is from the center of the image
* The images folder contains the following images. Open them to see what they have. The naming is as follows:
  * straight.jpg - car should got straight
  * left.jpg - car should turn left
  * right.jpg - car should turn right
* Open which_way.py to see some example code. Edit the image being used to see different output. Run it as follows (hit enter to close the image window):
    ```sh
    python3 which_way.py
    ```
## TODO
* Verify if any of these steps are worth it, i.e. start with working real world data/car and experiment. Calibration may be necessary for good performance. It may be that it is difficult to threshold well without calibration. Maybe we could just get better at thresholding? Consider processing performance/delay in the performance trade off as well as the actual car/sontro lsignal performance
* Investigate ways to smooth noise/predict control basedo n images/control signal output with less image processing (maybe right/left/straight is good enouggh with a kalman or soemthing)?
*  [Camera Calibration](https://docs.opencv.org/2.4/doc/tutorials/calib3d/camera_calibration/camera_calibration.html)
* [Color Correction](https://stackoverflow.com/questions/18897730/how-i-make-color-calibration-in-opencv-using-a-colorchecker)
* [Color & Contrast Correction](https://stackoverflow.com/questions/19363293/whats-the-fastest-way-to-increase-color-image-contrast-with-opencv-in-python-c)
* [More contrast nehancement etc](https://www.slideshare.net/yuhuang/image-color-correction-contrast-adjustment)

## Reading images from the raspi

* Google for reading images from an ip cam
* Needs to be a jpeg stream? or .mjpg for the easiest version
* check out [this code sample](https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv) that uses OpenCV  
  ```python
  cap = cv2.VideoCapture("http://192.168.18.37:8090/test.mjpeg")
  ```
  
## Sources
  
* [Installing OpenCV](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-18-04/)
* [Testing OpenCV](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html)
* [How to find colors in an image](https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/)
* [How to find the center of a blob](https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/)
* [Camera Calibration](https://docs.opencv.org/2.4/doc/tutorials/calib3d/camera_calibration/camera_calibration.html)
