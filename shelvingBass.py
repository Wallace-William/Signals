#William Wallace

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

config = open("shelvingConfig.txt","r")
music = config.readline()
music = music.rstrip('\n')
gain = config.readline()
gain = int(gain)
cutoff = config.readline()
cutoff = int(cutoff)

data, fs = sf.read(music)
fft = np.fft.fft(data)

length = len(fft)
#y-axis max
maxa = max(np.absolute(fft))+100 

#Fundamental Frequency
x = fs/length
x_axis = np.arange(length)
x_axis = x*x_axis

#Shelving Filter
theta = (2*np.pi*cutoff)/fs
mu = 10**(gain/20)
gamma = (1-(4/1+mu)*np.tan(theta/2))/(1+(4/1+mu)*np.tan(theta/2))
alpha = (1-gamma)/2

u = np.empty(length)
y = np.empty(length)

u[-1] = 0
data[-1] = 0

for n in range(0, length):
    u[n] = alpha*(data[n]+data[n-1])+gamma*u[n-1]
    y[n] = data[n]+(mu-1)*u[n]

#Apply fft to filtered output
fft_filter = np.fft.fft(y)

plt.figure(1)
plt.subplot(1,2,1)
plt.title('Original')
plt.ylim([0, maxa])
plt.xlim([0, length*x/4])
plt.xlabel('Hz')
plt.plot(x_axis, np.absolute(fft))

plt.subplot(1,2,2)
plt.title('Filtered')
plt.ylim([0,maxa])
plt.xlim([0,length*x/4])
plt.xlabel('Hz')
plt.plot(x_axis, np.absolute(fft_filter))

plt.tight_layout
plt.show()

sf.write('shelvingOutput.wav', y, fs)