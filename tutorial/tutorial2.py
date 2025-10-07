import cv2
img = cv2.imread("assets/re4.jpg", -1)

print(img.shape) 
print(img[0][100])

# Manipulating image pixels through looping
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [255, 255, 255]

# copy parts of an image:
tag = img[50:100, 50:100]
img[100:150, 10:60] = tag

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


''' 
Explaination of Tutorial 2:
============================================================================================================

Line 4: Displays the (height, width, channels) of the picture. OpenCV uses BGR instead of RGB

Line 5: Displays the BGR values for a specific pixel at index [row][column]. Rows and column can also 
    be sliced, [row:row][column:column]

Line 6: Loops across the rows and columns to change BGR values of each pixel. In this case, we are looping
    on the first 100 rows, the whole entire column, and changing each BGR value to [255, 255, 255] (white).  

Line 13-14: Copies part of the image from index [row:row, height:height] and pasting it onto another set 
    index at [row:row, height:height]. In this case, we are copying from indices [50:100, 50:100] and 
    pasting it at location [100:150, 10:60]. Do note that indice ratio has to be exactly the same. 
    

'''