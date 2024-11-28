#Import necessary libraries
import cv2
import controller as cnt  #Custom module for LED control
from cvzone.HandTrackingModule import HandDetector

#Initialize the hand detector
detector=HandDetector(detectionCon=0.8,maxHands=1)

#Open the default webcam
video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read() #Capture a frame from video stream
    frame=cv2.flip(frame,1) #Flip the frame
    hands,img=detector.findHands(frame) #Detect hands in the frame

    #Process the detected hands
    if hands:
        lmList=hands[0] #Get the list for first detected hand
        fingerUp=detector.fingersUp(lmList) # Gives which fingers of the detected hands are raised

        print(fingerUp)
        cnt.led(fingerUp) #Control LEDs based on finger count

        #Display finger count text on the frame 
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)    
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA) 

    #Display the processed frame
    cv2.imshow("frame",frame)

    #Wait for a key press with a delay of 1 millisecond
    k=cv2.waitKey(1)

    #Break the loop if 'k' key is pressed (optional exit key)
    if k==ord("k"):
        break
#Release the video capture object
video.release()

cv2.destroyAllWindows()
