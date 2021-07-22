import cv2 ,time

video=cv2.VideoCapture(0)   #This method triggers video capture object, 0 refers to the camera ,if there are 2 cams you would pass 1

a=1  # flag to check the no of frames generated

while True:
    a=a+1
    check,frame=video.read() #check returns boolean indicates if the video is running(True) or not(False)...Frame returns the numpy array of the each frame the video captures

    print(check)
    print(frame)

    #time.sleep(3)
    #cv2.imshow("Capturing",frame) #prints the first frame of the vdio

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts the color frame to gray

    cv2.imshow("gray_img",gray)

    key=cv2.waitKey(1)  # 3 milliseconds ..so its captures every frame for 3 millisecs
    
    if key==ord("q"): #exits the video if users press q
        break

print("no of frames:"+str(a))
video.release() #releases the video
cv2.destroyAllWindows()
