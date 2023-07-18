import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("frontalface-haarcascade.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    if ret == False:
        break

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_frame = face_cascade.detectMultiScale(gray_frame, 1.5, 3) #x,y,w,h

    for (x,y,w,h) in face_frame:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 148, 50), 3)

    cv2.imshow("me", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()