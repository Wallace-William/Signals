#William Wallace

import numpy as np
import soundfile as sf
import glob
from scipy import signal
import operator

#Read and get values for the testSong
data, fs = sf.read('testSong.wav')
f_test, t_test, Sxx_test = signal.spectrogram(data, fs=fs, nperseg=int(0.5*fs))

#Produce testSong signature
test_sig = np.zeros(t_test.size)
for n in range(0, t_test.size):
    #Enumerate Sxx by window, find max amplitude in window, get index of max to find frequency
    max_index, max_value = max(enumerate(Sxx_test[:,n]), key=operator.itemgetter(1))
    #Get corresponding frequency value using previously found index
    test_sig[n] = f_test[max_index]

#Count number of songs in directory for norm array size
count = 0
for name in glob.glob('song-*.wav'):
    count +=1
    
#Array for calculated song norms, as well as a list for the song names
norms = np.empty(count)
names = list()

#Find signature of all wav files in the format 'song-*.wav'
i = 0
for name in glob.glob('song-*.wav'):
    data, fs = sf.read(name)
    f, t, Sxx = signal.spectrogram(data, fs=fs, nperseg=int(0.5*fs))
    
    sig = np.zeros(t.size)
    for n in range(0, t.size):
        max_index, max_value = max(enumerate(Sxx[:,n]), key=operator.itemgetter(1))
        sig[n] = f[max_index]
    
    #Produce the 1-norm of the difference of test_sig and sig
    one_norm = 0
    for n in range(0, t.size):
        one_norm += np.absolute(sig[n]-test_sig[n])
    norms[i] = one_norm
    names.append(name)
    i+=1

#Create sorted index array for output
index = sorted(range(len(norms)), key=lambda k: norms[k])

#Print out sorted values based on index array 'index'
for n in range(0, norms.size):
    print(float(norms[index[n]]), names[index[n]])

        
       

