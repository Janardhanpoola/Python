import cv2,pandas

from datetime import datetime

video=cv2.VideoCapture(0)



first_frame=None

status_list=[None,None]   #list to capture the 0's(no movement) and 1's(movement).......[None,None] this is because of IndexError in line 56

times=[] #list to capture the switching of 0's and 1's 

df=pandas.DataFrame(columns=["START","END"])

#print(df)

while True:
    check,frame=video.read()

    #print(check)
    #print(frame)
    status=0

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray=cv2.GaussianBlur(gray,(21,21),0) #this will blur the frames captured to increase accuracy..2nd is tuple of hi8 and width..3rd is std. deviation

    if first_frame is None:  #capturing the first frame and storing it to a variable first_frame
        first_frame=gray  
        continue 

    #calculate the diff b/w 1st and 2nd frame
    delta_frame=cv2.absdiff(first_frame,gray)
    
   #Applying the threshold mtd i.e if the diff. is >30 then mark the frames as white(moving object)...if <30 black (no motion)

    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]  #1st is frame,2nd is threshold value i.e (>30)..,3rd is color(255 is white),4th is thres_binary mtd

    thresh_delta=cv2.dilate(thresh_delta, None, iterations=4)  #to smooth the threshold frame

    #finding the contours that are less than 1000 frames
    (cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<10000:  #if pixel is <10000 then check for other pixels and draw rectangle
            continue
        
        status=1

        (x,y,w,h)=cv2.boundingRect(contour) #taking the rectangle corners

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)


    status_list.append(status)  
    
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())        

    cv2.imshow("first",first_frame)
    cv2.imshow("GRAY",gray)
    cv2.imshow("DELTA",delta_frame)
    cv2.imshow("THRESHOLD",thresh_delta)
    cv2.imshow("Original",frame)


    key=cv2.waitKey(1)
    if key==ord("q"):
        if status==1:
            times.append(datetime.now())
        break


print(status_list)
print(times)

#Iterate through times list and append it to dataframe
for i in range(0,len(times),2):   #step is 2
    df=df.append( {"START":times[i],"END":times[i+1]} ,ignore_index=True )

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()