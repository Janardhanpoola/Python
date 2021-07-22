import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #this  xml file has face attributes

img=cv2.imread("news.jpg")

grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #greay image

faces=face_cascade.detectMultiScale(grey_img,
scaleFactor=1.1,
minNeighbors=5) #scale factor is decreasing the scale by 5% for face search.Min neighbours is how many neighboues to search around the window

print(type(faces)) #prints the coordinates of the face
print(faces)



for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)  #recognizing face i.e drwaing green rectangle around the face.
#takes 4 arguments. 1st is image,2 is tuple of top left corner of the face,3 is tuple of bottom right coodinates,4 is (B,G,R) color,5th is width of the rectangle 

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))


cv2.imshow("FACE",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

