import cv2
import glob
images=glob.glob("*.jpg")

for img in images:
    print(img)
    image=cv2.imread(img,0)
    resized=cv2.resize(image,(100,100))
    cv2.imshow("BATCH",resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()  
    cv2.imwrite("Modified_"+img,resized)  

#for image in images:
#    img=cv2.imread(image,0)
#    re=cv2.resize(img,(100,100))
#    cv2.imshow("Hey",re)
#    cv2.waitKey(500)
#    cv2.destroyAllWindows()
#    cv2.imwrite("resized_"+image,re)