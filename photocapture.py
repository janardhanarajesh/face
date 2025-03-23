import cv2
import keyboard
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("there is a error in opening the camera")
else:
    k=keyboard.read_key()
    if k=="enter":
        ret,frame=cap.read()
        frame=cv2.flip(frame,1)
        if ret:
            # pass
            # cv2.imshow("captured image",frame)
            cas=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\face_detector.xml")
            faces=cas.detectMultiScale(frame,1.1,4)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),10)
            ln=len(faces)
            print(ln)
            cv2.putText(frame,f"detected {ln} faces",(180,150),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0))
            cv2.imshow("detected face",frame)
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()