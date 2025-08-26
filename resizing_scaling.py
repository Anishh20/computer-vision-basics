import cv2 as cv 
import numpy as np 

capture=cv.VideoCapture("videos/dogvideo1.mp4")

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame=capture.read()

    frame_resize=rescaleFrame(frame)

    cv.imshow("video",frame_resize)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break    


capture.release()
cv.destroyAllWindows()