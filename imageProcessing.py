#William Wallace

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

N = 10	#Moving average value

h_low = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
h_high = [1, -1]


boat = plt.imread('boat.512.tiff')
plt.figure(0)
plt.imshow(boat)
plt.title('Boat Original Image')
plt.show()

#Low Pass
b_size = boat[0,:].size
out = np.empty((0, b_size))
for line in range(0, b_size):
    result = np.convolve(boat[line],np.ones((N,))/N)
    result = result[0:b_size]
    out = np.append(out, [result], axis=0)
plt.figure(1)
plt.imshow(out)
plt.title('Boat Low Pass')
plt.show()

#High Pass
out = np.empty((0, b_size))
for line in range(0,b_size):
    result = np.convolve(boat[line], h_high)
    result = result[0:b_size]
    out = np.append(out, [result], axis=0)
plt.figure(2)
plt.imshow(out)
plt.title('Boat High Pass')
plt.show()

##############################################################
clock = plt.imread('clock-5.1.12.tiff')
plt.figure(3)
plt.imshow(clock)
plt.title('Clock Original Image')
plt.show()

#Low Pass
c_size = clock[0,:].size
out = np.empty((0, c_size))
for line in range(0, c_size):
    result = np.convolve(clock[line],np.ones((N,))/N)
    result = result[0:c_size]
    out = np.append(out, [result], axis=0)
plt.figure(4)
plt.imshow(out)
plt.title('Clock Low Pass')
plt.show()

#High Pass
out = np.empty((0, c_size))
for line in range(0,c_size):
    result = np.convolve(clock[line], h_high)
    result = result[0:c_size]
    out = np.append(out, [result], axis=0)
plt.figure(5)
plt.imshow(out)
plt.title('Clock High Pass')
plt.show()

##############################################################
man = plt.imread('man-5.3.01.tiff')
plt.figure(6)
plt.imshow(man)
plt.title('Man Original Image')
plt.show()

#Low Pass
m_size = man[0,:].size
out = np.empty((0, m_size))
for line in range(0, m_size):
    result = np.convolve(man[line],np.ones((N,))/N)
    result = result[0:m_size]
    out = np.append(out, [result], axis=0)
plt.figure(7)
plt.imshow(out)
plt.title('Man Low Pass')
plt.show()

#High Pass
out = np.empty((0, m_size))
for line in range(0,m_size):
    result = np.convolve(man[line], h_high)
    result = result[0:m_size]
    out = np.append(out, [result], axis=0)
plt.figure(8)
plt.imshow(out)
plt.title('Man High Pass')
plt.show()
##############################################################
tank = plt.imread('tank-7.1.07.tiff')
plt.figure(9)
plt.imshow(tank)
plt.title('Tank Original Image')
plt.show()

#Low Pass
t_size = tank[0,:].size
out = np.empty((0, t_size))
for line in range(0, t_size):
    result = np.convolve(tank[line],np.ones((N,))/N)
    result = result[0:t_size]
    out = np.append(out, [result], axis=0)
plt.figure(10)
plt.imshow(out)
plt.title('Tank Low Pass')
plt.show()

#High Pass
out = np.empty((0, t_size))
for line in range(0,t_size):
    result = np.convolve(tank[line], h_high)
    result = result[0:t_size]
    out = np.append(out, [result], axis=0)
plt.figure(11)
plt.imshow(out)
plt.title('Tank High Pass')
plt.show()

###############################################################

#Original Image
darin = plt.imread('darinGrayNoise.jpg')
plt.figure(12)
plt.imshow(darin)
plt.title('Darin Original Image')
plt.show()

#Lowpass Filter
darin_L = darin[0,:].size
darin_H = darin[:,0].size

out = np.empty((0, darin_L))
for line in range(0, darin_H):
    result = np.convolve(darin[line],np.ones((N,))/N)
    result = result[0:darin_L]
    out = np.append(out, [result], axis=0)
plt.figure(13)
plt.imshow(out)
plt.title('Darin Low Pass')
plt.show()

#Median Filter
outputImage = ndimage.median_filter(darin, 5)
plt.figure(14)
plt.imshow(outputImage)
plt.title('Darin with Median Filter')
plt.show()
