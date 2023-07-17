import cv2

cap = cv2.VideoCapture(0)

##dizinden video ekleyip gösterebiliriz
#cap = cv2.VideoCapture("video.mp4")

##video bittikten sonra hata vermeden ekranı kapatır
# if ret == 0:
#    break


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
         break


cap.release()
cv2.destroyAllWindows()