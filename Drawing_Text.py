import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3),dtype="uint8")

# cv.imshow("blank",blank)


#painting a image 

# blank[0:50]=0,255,0
# cv.imshow("green",blank)

#drawing a rectangle

# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow("rectangle",blank)

#similarly we can draw circle,line,text too 

#text 

cv.putText(blank,"hello my name is anish",(0,250),cv.FONT_HERSHEY_TRIPLEX,0.6,(0,0,255),3)
cv.imshow("text",blank)






cv.waitKey(0)