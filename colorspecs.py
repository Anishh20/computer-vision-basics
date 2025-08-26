import cv2

img = cv2.imread("images/cat.jpg")

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


# Convert to different color spaces

frame_resize=rescaleFrame(img,scale=0.5)
rgb = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2LAB)
ycrcb = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2YCrCb)

# Show results
cv2.imshow("Original BGR", img)
cv2.imshow("RGB", rgb)
cv2.imshow("GRAY", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)
cv2.imshow("YCrCb", ycrcb)

cv2.waitKey(0)
cv2.destroyAllWindows()
