import cv2 as c
im=c.imread(r"C:\Users\dell\Desktop\rajesh\par.jpg")
print(im.shape[:2])
(r,g,b)=im[250,250]
bk=im[250,250,0]
print(bk)
print(f"{r,g,b}")
sr=c.resize(im,(1080,600))
k=c.imwrite("parentnew.jpg",sr)
if k:
    print("resized")
sr=c.circle(im,(250,250),10,(255,200,0),10)
c.imwrite("parentnew.jpg",sr)
sr=c.putText(im,"rajesh",(250,250),c.FONT_HERSHEY_COMPLEX,4,(0,0,255))
k=c.imwrite("parentnew.jpg",sr)
print(k)
c.imshow("new image",sr)
c.waitKey(0)
c.destroyAllWindows()