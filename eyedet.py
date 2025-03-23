import cv2
import keyboard
import time
vid=cv2.VideoCapture(0)
if not vid.isOpened():

    print("error in opening camera")
else:
        time.sleep(0.1)
        ret,img=vid.read()
        img=cv2.flip(img,1)

        if ret:
            cap1=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\haarcascade_lefteye_2splits.xml")
            eye=cap1.detectMultiScale(img,1.1,5)
            cap2=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\face_detector.xml")
            faces=cap2.detectMultiScale(img,1.1,5)
            cap3=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\haarcascade_smile.xml")
            smile=cap3.detectMultiScale(img,1.1,100)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
            for (x,y,w,h) in eye:
                 cv2.circle(img,(x+w-30,y+h-20),20,(0,250,0),2)
            for (x,y,w,h) in smile:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
            ln1=len(eye)
            ln2=len(faces)
            ln3=len(smile)
            print(f"The detected object has {ln2} faces , {ln1} eyes and it is has {ln3} mouth")
            
            cv2.imshow("detected face and eyes",img)
vid.release()
cv2.waitKey(0)

cv2.destroyAllWindows()