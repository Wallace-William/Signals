#William Wallace

import numpy as np
from scipy.io import wavfile

#0.5sec with 1/8000 step rate
t = np.arange(0, 0.5, 1/8000)

#Produce cosine waves for each note
C = np.cos(2*np.pi*(440*2**((52-49)/12))*t)
D = np.cos(2*np.pi*(440*2**((59-49)/12))*t)
E = np.cos(2*np.pi*(440*2**((61-49)/12))*t)
F = np.cos(2*np.pi*(440*2**((57-49)/12))*t)
G = np.cos(2*np.pi*(440*2**((56-49)/12))*t)
A = np.cos(2*np.pi*(440*2**((54-49)/12))*t)

#Create sequence of notes for concatenation (24 notes, 0.5sec each, total runtime = 12sec)
wave = (C, C, D, D, E, E, D, D, F, F, G, G, A, A, G, C, D, D, F, F, G, G, A, A)

#Insert wave variable into concatenate function (the list could also be inserted here)
twinkle = np.concatenate(wave)

#write the concatenated cosine signal to a .wav file with a sample rate of 8000
wavfile.write('twinkle.wav',8000,twinkle)

