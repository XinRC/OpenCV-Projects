import cv2

cap = cv2.VideoCapture(0) 

# Begin displaying video capture
while True:
  ret, frame = cap.read() 

  sframe = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
  
  cv2.imshow('frame', frame)
  #cv2.imshow('sframe', sframe)
  

  if cv2.waitKey(1) == ord('q'): 
    break


cap.release() #release camera resource -> allows another resource to use it

cv2.destroyAllWindows()


'''
Explaination for Tutorial 3: 
======================================================================================================

Line 3: Initializes a variable with the data from a webcame's video capture. Within the parameters, 
    there are several inputs that can be used
        integer || 0 : Dictates to use camera (0) as the video capture feed. You can specify to use 
            which camera
        "file name" : Dictates to use a video file as the video capture feed 

Line 6: Loops over video capture frames until Line 16 is is ran. 

Line 7: Returns "ret" and "frame" - ret is used to determine if the webcam is accessible, and the
    frame is used to display the actual footage.

Line 9: Creates a smaller display frame by resizing it by 0.5 on both the width and height

Line 11-12: Depending on which is commented out, the program will display active video capture

Line 15-16: If specifically pressed the key under order(''), then the footage would break. In this
    case, if we pressed the letter 'q' on the keyboard, it would break the video capture feed.

Line 19: Releases the camera resources, allowing another application to use it


'''