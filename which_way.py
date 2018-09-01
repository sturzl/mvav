import cv2 as cv
import numpy as np

## Read the image, find the red lane

imageName = 'straight_nobackground.jpg'
# imageName = 'right.jpg'
# imageName = 'left.jpg'

image = cv.imread('images/' + imageName)
# cv.imshow('Original image',image)
# cv.waitKey(0)
# print('Done')

blurredImage = cv.medianBlur(image,99)
# cv.imshow('Blurred Image',blurredImage)
# cv.waitKey(0)
# print('Done')


# redLane = cv.inRange(blurredImage,lower_red,upper_red)
blurredImageHSV = cv.cvtColor(blurredImage, cv.COLOR_BGR2HSV)
# cv.imshow('HSV Image',blurredImageHSV)
# cv.waitKey(0)
# print('Done')

# consider using a gaussian threshold after the mask to erase bits and spots)
# red is 4,60,94  38,99,94
# brown is 20,76,64  64, 96, 79
lower_red = np.array([0,30,60]) 
upper_red = np.array([10,180,255])

maskRedLane = cv.inRange(blurredImageHSV, lower_red, upper_red)
# ret,thresholdRedLane = cv.adaptiveThreshold(redLaneHsv,220,255,cv.gaussian something)

cv.imshow('Thresholded image',maskRedLane)
cv.waitKey(0)
print('Done')


momentsForLane = cv.moments(maskRedLane)
laneHorizontalCenter = int(momentsForLane["m10"] / momentsForLane["m00"])
imageHorizontalCenter = len(image[0])/2 # width of image

print('laneHorizontalCenter: ' + str(laneHorizontalCenter))
print('imageHorizontalCenter: ' + str(imageHorizontalCenter))

if(laneHorizontalCenter < (imageHorizontalCenter - 10)):
	print('Turn left')
elif(laneHorizontalCenter > (imageHorizontalCenter + 10)):
	print('Turn right')
else:	
	print('Go straight')