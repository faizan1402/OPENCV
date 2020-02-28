# Bluring the imgage

import cv2

import numpy as np

img =cv2.imread("lena.png")

cv2.imshow("Original Image",img)

cv2.waitKey(0)

#How to blur the imgblur

# useing the Kernel function through img is blur Kernel matrix value is increase then img is more times 

#Syntax-

#Kernel_dimension=np.ones((size of matrix to pass ),np.float 32)/size of matrix devide

kernel_3x3 =np.ones((3,3),np.float32)/9

# We use the cv2.filter 2D to convolve the kernel with an image
#filter function used  the 2D 
# cv2.filter2D(img,deft,kernel function)
blurred =cv2.filter2D(img,-1,kernel_3x3)
#read the blurred img
cv2.imshow('3x3 Kernel Blurring',blurred)

cv2.waitKey(0)

kernel_10x10 =np.ones((10,10),np.float32)/100

blurred =cv2.filter2D(img,-1,kernel_10x10)

cv2.imshow("10x10 kernel Blurring",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows() 

 
