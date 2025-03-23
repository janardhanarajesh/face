import cv2
import keyboard
cap=cv2.VideoCapture(0)
class1=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\haarcascade_lefteye_2splits.xml")
class2=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\face_detector.xml")
class3=cv2.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\haarcascade_smile.xml")

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    eye=class1.detectMultiScale(frame,1.1,5)
    fac=class2.detectMultiScale(frame,1.1,5)
    smile=class3.detectMultiScale(frame,1.1,100)

    for (x,y,w,h) in fac:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
    for (x,y,w,h) in smile:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    for (x,y,w,h) in eye:
        cv2.circle(frame,(x+w-30,y+h-30),20,(0,255,0),4)
    if len(smile)==1:
        print(f"detected object has {len(fac)} faces , {len(eye)} eyes and the object is smiling")
    elif len(smile)==0:
        print(f"detected object has {len(fac)} faces , {len(eye)} eyes and the object is not smiling")


    cv2.imshow("detected",frame)
    if cv2.waitKey(1) & 0xff ==27:
        break
cap.release()
cv2.destroyAllWindows() 

