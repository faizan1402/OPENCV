# How to image write and copy or clone
import cv2
img =cv2.imread('lena.jpg')
cv2.imshow('original image',img)
#Temporay file create (means previous langauge c++ file handling concept related)
cv2.imwrite('output.jpg',img)

cv2.waitkey(0)

cv2.destroy AllWindows()
