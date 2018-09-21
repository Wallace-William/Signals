#William Wallace

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import freqz

fc = 7500
L = 101
M = L - 1

data, fs = sf.read('P_9_2.wav')
ft = fc/fs

h = np.empty(L+1)
n = 0
while n < L:		#Low pass filter
    if n != M/2:
        h[n] = np.sin(2*np.pi*ft*(n-(M/2)))/(np.pi*(n-(M/2)))
    else:
        h[n] = 2*ft
    n+=1

w = np.empty(L+1)	
n = 0
while n < L:		#Hamming Window
    w[n] = 0.54 - 0.46*np.cos(2*np.pi*n/M)
    n+=1

h_new = h*w

x, y = freqz(h, 1)
x_1, y_1 = freqz(h_new, 1)

plt.figure()		#Freq Plot
plt.title('Frequency Response')
plt.plot(x, abs(y))
plt.plot(x_1, abs(y_1))
plt.show()

data = np.convolve(data, h_new)


sf.write('cleanMusic.wav', data, fs)	#Clean music .wav
