import cv2 as cv
image = cv.imread('images/tapered_nobackground.jpg')
cv.imshow('image',image)
cv.waitKey(0)
cv.destroyAllWindows()
print('Great Success!')
