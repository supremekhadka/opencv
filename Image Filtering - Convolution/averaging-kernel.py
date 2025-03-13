import cv2
import numpy as np
 
image = cv2.imread('supreme.JPG')
 
#  check for image
if image is None:
    print('Could not read image')
 
# averaging kernel 
kernel2 = np.ones((15, 15), np.float32) / 225  # 15x15 Kernel X 1/225 
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 800, 800)
cv2.namedWindow("Kernel Blur", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Kernel Blur", 800, 800)

cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
     
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()