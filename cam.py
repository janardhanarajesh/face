import cv2
import keyboard
while True:
    x=cv2.VideoCapture(0)
    k,y=x.read()
    cv2.imshow("cam",y)
    if cv2.waitKey(1) & 0XFF==ord('x'):
        break
x.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
    