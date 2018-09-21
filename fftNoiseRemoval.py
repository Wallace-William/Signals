#William Wallace

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import freqz

data, fs = sf.read('P_9_2.wav')
fft = np.fft.fft(data)

plt.figure()
plt.plot(np.absolute(fft.real))
plt.title('FFT Values')
plt.show()

median = len(fft.real)
median = median/2
median = int(median)
offset = 10000
leftbound = median-offset
rightbound = median+offset

for x in range(leftbound, rightbound):
    fft[x] = 0

plt.figure()
plt.plot(np.absolute(fft.real))
plt.title('Cleaned FFT values')
plt.show()

data = np.fft.ifft(fft).real


sf.write('cleanMusic.wav', data, fs)    #Clean music .wav

