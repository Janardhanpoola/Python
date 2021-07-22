import cv2
img=cv2.imread("lion.jpg",0)  #0 for grey scale, 1-->RBG(color)
print(img)
print(img.shape)#prints no.of rows&cols

resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2) ))
cv2.imshow("LION",resized_img)   #displays the image 

cv2.waitKey(2000) #waits for 2 secs 
cv2.imwrite("RESIZED.jpg",resized_img) #writing the resized img to a new image

print(resized_img.shape)

#cv2.waitKey(0) #this means the image closes on pressing any key
cv2.destroyAllWindows() # destroys the window