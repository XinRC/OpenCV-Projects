import cv2 

img = cv2.imread("assets/googleLogo.webp", -1) 

# image modifications:
img = cv2.resize(img, (600, 400)) 
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# saving/displaying image
cv2.imwrite("new_img.jpg", img)

cv2.imshow('Image', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()


''' 
Explaination of Tutorial 1:
=============================================================================================

Line 1: Imports the OpenCV module into the IDE. This allows us to utilize its libraries

Line 2: Creates a variable that will hold the image we want to read. Be sure to have the 
    image saved in the same directory as the program you are running
        -1 || cv2.IMREAD_COLOR : (default) loads image in colored
        0 || cv2.IMREAD_GRAYSCALE : loads image in grayscale
        1 || cv2.IMREAD_UNCHANGED : loads image in colored (allows for transparency)

Line 5: Redefines the original variable, allowing for us to resize the image
        cv2.resize(img, (width, height))
        cv2.resize(img, (0, 0), fx = ratio, fy = ratio) where ratio is a resizing int/float

Line 7: Redefines the original variable, allowing for us to rotate the image
        .ROTATE_90_CLOCKWISE
        .ROTATE_90_COUNTERCLOCKWISE
        .ROTATE_180

Line 10: Saves the image into current folder with the name ""

Line 12: Displays the image with the title ""

Line 13: Allows us to wait a certain amount of milliseconds before going to the next set of    
    instructions
        0 represents infinite time in this case

Line 14: Closes all window/s

'''