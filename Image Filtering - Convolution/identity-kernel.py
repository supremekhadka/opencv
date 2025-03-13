import cv2
import numpy as np
 
image = cv2.imread('supreme.JPG')
 
#  check for image
if image is None:
    print('Could not read image')
 
#  identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 800, 800)
cv2.namedWindow("Identity", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Identity", 800, 800)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
     
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()