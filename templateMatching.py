#William Wallace

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import feature

ERBfull = mpimg.imread('ERBwideColorSmall.jpg')
ERBpart = mpimg.imread('ERBwideTemplate.jpg')

#Convert both images to grayscale
R = ERBfull[:,:,0]
G = ERBfull[:,:,1]
B = ERBfull[:,:,2]
img_gray = R*299./1000+G*587./1000+B*114./1000

R1 = ERBpart[:,:,0]
G1 = ERBpart[:,:,1]
B1 = ERBpart[:,:,2]
img_gray_temp = R1*299./1000+G1*587./1000+B1*114./1000

#This caused problems with the template image
#img_gray_temp = np.average(ERBpart, weights=[0.299,0.587,0.114], axis=2)

plt.figure(0)
plt.gray()
plt.title('ERBwide')
plt.imshow(img_gray)
plt.show()

plt.figure(1)
plt.gray()
plt.title('Template')
plt.imshow(img_gray_temp)
plt.show()

#Apply match_template function
output = feature.match_template(img_gray, img_gray_temp)

#Dimensions of Larger Image
length = img_gray[0,:].size
width = img_gray[:,0].size

#Dimensions of Template Image
length_t = img_gray_temp[0,:].size
width_t = img_gray_temp[:,0].size

#Find location of best fit
row = np.argmax(np.max(output, axis=1))
column = np.argmax(np.max(output, axis=0))
print("row =", row)
print("column =", column)    

#Remove template from larger image
for i in range(row, row+length_t):
    for j in range(column, column+width_t):
        img_gray[i][j] = 0

plt.figure(2)
plt.gray()
plt.title('ERBwide minus Template')
plt.imshow(img_gray)
plt.show()
 
