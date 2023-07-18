import cv2
import numpy as np

def nothing(x):
    pass

canvas = np.zeros((1024, 1024, 3), dtype=np.uint8)
cv2.namedWindow('Color Palette')
switch = "0: OFF, 1:ON"

cv2.createTrackbar('R', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('G', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('B', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('Switch', 'Color Palette', 0, 1, nothing)

while True:
    r = cv2.getTrackbarPos("R", "Color Palette")
    g = cv2.getTrackbarPos("G", "Color Palette")
    b = cv2.getTrackbarPos("B", "Color Palette")
    s = cv2.getTrackbarPos("Switch", "Color Palette")

    if s == 0:
        canvas[:] = 0

    if s == 1:
        canvas[:] = [b, g, r]

    cv2.imshow("Color Palette", canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
