#prerequisites
#"Opencv
#"PyAutoGUI
#Its possible to perform actions without actually giving any input though touchpad or mouse.we can use color detection to scroll screen.when a certain color is detected by the program during execution the screen starts to scroll on its own.
#Approach
#import module
#Use cv2 to capture video,here to use default webcam use 0,and for any other cam use 1
#Read the capture video and store the video frame in a variable
#get every color of the frame.
#create a mask of the color required to take as input to scroll using their acceptable color ranges.here its taken as green.
#get contours and hierarchy from mask
#pass contours using for loop and calculate the area
#add scroll mechanism when required color is detected(Green here)
#show the frame using cv2.imshow()and pass the frame name and the frame variable to show every captured frame,put the frame capture process in a while loop.to come out of the process use a wait key and break statement.
#then stop the window of webcam.

import cv2
import numpy as np
import pyautogui

low_green = np.array([25,52,72])
high_green = np.array([102,255,255])

cap = cv2.VideoCapture(1)

prev_y = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame or end of video reached.")
        break
    # Proceed with cv2.cvtColor(frame, ...)

    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,low_green,high_green)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if y < prev_y:
                 pyautogui.press("space")
            prev_y = y
        cv2.imshow("frame",frame)
        if cv2.waitKey == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
   # cap.closeAllWindow()