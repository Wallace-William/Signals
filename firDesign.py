#William Wallace

import numpy as np
import matplotlib.pyplot as plt

fs = 2000

#Lowpass Filter
fc = 50
L = 21
M = L - 1
ft = fc/fs


csv = np.genfromtxt('data-filtering.csv',delimiter=",")

t = np.arange(0, 1, 1/fs)	
x = np.cos(2*np.pi*4*t) 	#4Hz Cosine


w = np.empty(L+1)	#Set up filter weight array
n = 0
while n < L:		#Lowpass filter weight equation
    if n != M/2:
        w[n] = np.sin(2*np.pi*ft*(n-(M/2)))/(np.pi*(n-(M/2))) 
    else:
        w[n] = 2*ft
    n+=1

low = np.convolve(csv,w)
plt.figure(1)
plt.subplot(3, 1, 1)
plt.title("original signal")
plt.plot(csv)

plt.subplot(3, 1, 2)
plt.title("4 Hz signal")
plt.plot(x)

plt.subplot(3, 1, 3)
plt.title("application of lowpass filter")
plt.plot(low)

plt.tight_layout()
plt.show()

#Highpass Filter
fc_High = 280
L_High = 21
M = L_High - 1
ft_High = fc_High/fs 


y = np.cos(2*np.pi*330*t)

u = np.empty(L_High+1)
n = 0

while n < L_High:
    if n!= M/2:
        u[n] = -np.sin(2*np.pi*ft_High*(n-(M/2)))/(np.pi*(n-(M/2)))
    else:
        u[n] = 1-2*ft_High
    n+=1
z = 100;

csv = csv[0:z]
y = y[0:z]

high = np.convolve(csv,u)
high = high[0:z]

plt.figure(2)
plt.subplot(3, 1, 1)
plt.title("original signal")
plt.plot(csv)

plt.subplot(3, 1, 2)
plt.title("330 Hz signal")
plt.plot(y)

plt.subplot(3, 1, 3)
plt.title("application of highpass filter")
plt.plot(high)

plt.tight_layout()
plt.show()
