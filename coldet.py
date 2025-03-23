import cv2
import numpy as np
import keyboard
lower_red=np.array([0,120,70])
upper_red=np.array([10,255,255])
lower_red2=np.array([170,120,70])
upper_red2=np.array([180,255,255])

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_red,upper_red)+cv2.inRange(hsv,lower_red2,upper_red2)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("result",result)
    # cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    # if np.any(mask):
        
    #     cv2.waitKey(0)
        
    #     break
    
    if cv2.waitKey(1) & 0Xff==27:
        break
cap.release()
cv2.destroyAllWindows()