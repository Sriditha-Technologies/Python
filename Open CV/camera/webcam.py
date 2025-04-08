import datetime
import cv2,times
first_frame=None
status_list=[None,None]
time=[]
df.pandas.DataFrame(columns=['start','end'])
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussionBlur(gray,(21,21),0)
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        status_list.append(status)
        status_list=status_list[-2:]
        if status_list[-1]==1 and status_list[-2]==0:
            times.append(datetime.now())
        if status_list[-1]==1 and status_list[-2]==0:
            times.append(datetime.now())
        print(status_list)
        print(times)
        for i in range(0,len(times),2):
        df=df.append({"start":times[i],"end":times[i+1]},ignore_index=True)
        df.to_csv("Times.csv")
        video.release()
        cv2.destroyAllWindows()