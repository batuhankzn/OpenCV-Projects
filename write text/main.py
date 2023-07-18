import cv2
import numpy as np

canvas = np.zeros((1024, 1024, 3), dtype=np.uint8) + 255
# print(canvas)

font1 = cv2.FONT_HERSHEY_SIMPLEX
redColor = (0, 0, 255)


cv2.putText(canvas, "batuhankzn", (256, 512), font1, 4, redColor)


cv2.imshow("Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
