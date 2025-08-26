import cv2 as cv
import numpy as np

# Load image
img = cv.imread("images/cat.jpg")

# ---------- 1. Translation ----------
def translate(img, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return shifted

translated = translate(img, 100, 50)

# ---------- 2. Rotation ----------
def rotate(img, angle, scale=1.0):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated = cv.warpAffine(img, M, (w, h))
    return rotated

rotated = rotate(img, 45)

# ---------- 3. Resizing ----------
resized = cv.resize(img, (300, 300))

# ---------- 4. Flipping ----------
flip_horizontal = cv.flip(img, 1)   # Horizontal
flip_vertical = cv.flip(img, 0)     # Vertical
flip_both = cv.flip(img, -1)        # Both

# ---------- 5. Affine Transformation ----------
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1, pts2)
affine = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

# ---------- 6. Perspective Transformation ----------
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1, pts2)
perspective = cv.warpPerspective(img, M, (300,300))

cv.imshow("Original", img)
cv.imshow("Translated", translated)
cv.imshow("Rotated", rotated)
cv.imshow("Resized", resized)
cv.imshow("Flipped H", flip_horizontal)
cv.imshow("Affine", affine)
cv.imshow("Perspective", perspective)

cv.waitKey(0)
