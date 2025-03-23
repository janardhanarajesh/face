import cv2 as c
face_cascade=c.CascadeClassifier(r"C:\Users\dell\Desktop\python\opencv\face_detector.xml")
img=c.imread('group.jpg')
faces=face_cascade.detectMultiScale(img,1.1,4)
for (x,y,w,h) in faces:
    c.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
print(len(faces))
c.imwrite("detectface.jpg",img)
print("photo sucessfully detected")
