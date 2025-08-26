import cv2 as cv 

img=cv.imread("images/cat.jpg")

cv.imshow("cat",img)

cv.waitKey(0)
