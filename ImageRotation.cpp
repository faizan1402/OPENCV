import cv2
import numpy as np
img =cv2.imread('lena.jpg')
height ,width =img.shape[:2]
roatation_matrix =cv2.getRotationMatrix2D((width/2,height/2,70,.5)

#getRotationMatrix2D is a function and rotate the img and (width,height ,angle,scaling factor)
#Means scaling factor will increase then img information destroy and scaling factor is decrease then img of information increase


#This roatation_matrix through image rotate
rotated_image =cv2.warpAffine(img,roatation_matrix,(width,height))

cv2.imshow("Original Image",img)
cv2.imshow("Rotated Image",rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()