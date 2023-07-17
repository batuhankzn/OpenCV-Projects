import cv2
import numpy as np

canvas = np.zeros((1024, 1024, 3), dtype=np.uint8) + 255
# print(canvas)


# line (çizgi)
cv2.line(canvas, (10, 10), (502, 502), (150, 50, 25))

# rectangle (kare)
cv2.rectangle(canvas, (50, 50), (200, 200), (50, 50, 50), thickness=-1)

# circle (daire)
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=5)

# triangle (üçgen)
num1 = (500, 600)
num2 = (600, 800)
num3 = (800, 500)

redColor = (0, 0, 255)
greenColor = (0, 128, 0)
yellowColor = (255, 255, 0)

cv2.line(canvas, num1, num2, redColor, 4)
cv2.line(canvas, num2, num3, greenColor, 4)
cv2.line(canvas, num3, num1, yellowColor, 4)

# polylines (çoklu çizgi)
dots = np.array([[[20, 950], [350, 150], [600, 450], [400, 100]]], np.int32)
pinkColor = [255, 182, 193]
cv2.polylines(canvas, dots, True, pinkColor, thickness=5)

# ellipse
center = (900, 600)
wide_Height = (20, 100)
angle = 90

cv2.ellipse(canvas, center, wide_Height, angle, 0, 360, greenColor, 4)

cv2.imshow("Board", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
