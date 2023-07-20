import cv2
from skimage.feature import hog
from skimage import exposure

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    _, hogImage = hog(frame_rgb, visualize=True, channel_axis=2)
    rescaled = exposure.rescale_intensity(hogImage, in_range=(0, 10))

    cv2.imshow("hog", rescaled)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()