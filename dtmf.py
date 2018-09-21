#William Wallace

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

fs = 8000
L = 64
fl = fs/2
filters = 7

csv = np.genfromtxt('tones.csv',delimiter=",")	#Get data from csv
with open('tones.csv') as f:
    file_content = f.read()
num_data = file_content.count(',')+1
num_data = int(num_data/fl)			#Get number of tones

csv = np.split(csv, num_data)			#Create arrays for each tone

#The seven filters
h_697 = np.empty(L+1)		
n = 0
while n < L:
    h_697[n] = 2/L*np.cos(2*np.pi*697*n/fs)
    n+=1

h_770 = np.empty(L+1)
n = 0
while n < L:
    h_770[n] = 2/L*np.cos(2*np.pi*770*n/fs)
    n+=1

h_852 = np.empty(L+1)
n = 0
while n < L:
    h_852[n] = 2/L*np.cos(2*np.pi*852*n/fs)
    n+=1

h_941 = np.empty(L+1)
n = 0
while n < L:
    h_941[n] = 2/L*np.cos(2*np.pi*941*n/fs)
    n+=1

h_1209 = np.empty(L+1)
n = 0
while n < L:
    h_1209[n] = 2/L*np.cos(2*np.pi*1209*n/fs)
    n+=1

h_1336 = np.empty(L+1)
n = 0
while n < L:
    h_1336[n] = 2/L*np.cos(2*np.pi*1336*n/fs)
    n+=1

h_1477 = np.empty(L+1)
n = 0
while n < L:
    h_1477[n] = 2/L*np.cos(2*np.pi*1477*n/fs)
    n+=1
 
#Find frequencies within csv using previous 7 filters
tone = np.empty(filters)
output = []
for i in range(0, num_data):
    note = csv[i]
    
    out0 = np.convolve(note, h_697)
    out1 = np.convolve(note, h_770)
    out2 = np.convolve(note, h_852)
    out3 = np.convolve(note, h_941)
    out4 = np.convolve(note, h_1209)
    out5 = np.convolve(note, h_1336)
    out6 = np.convolve(note, h_1477)

    tone[0] = np.mean(out0**2)			
    tone[1] = np.mean(out1**2)
    tone[2] = np.mean(out2**2)
    tone[3] = np.mean(out3**2)
    tone[4] = np.mean(out4**2)
    tone[5] = np.mean(out5**2)
    tone[6] = np.mean(out6**2)

    if tone[0] > tone[1]:			#Find the 2 highest mean outputs based on filters
        largest = tone[0]
        second_largest = tone[1]
    else:
        largest = tone[1]
        second_largest = tone[0]
    for item in tone[2:]:
        if item > largest:
            second_largest = largest
            largest = item
        elif largest > item > second_largest:
            second_largest = item

    num = 0					#Find index of the highest mean outputs
    for num in range(0,7):
        if largest == tone[num]:
            largest = num
        if second_largest == tone[num]:
            second_largest = num

    if largest == 0 or second_largest == 0:	#Search through filter bank based on found indexes
        if largest == 4 or second_largest == 4:
            output = np.append(output,'1')
        elif largest == 5 or second_largest == 5:
            output = np.append(output,'2')
        else:
            output = np.append(output,'3')
    elif largest == 1 or second_largest == 1:
        if largest == 4 or second_largest == 4:
            output = np.append(output,'4')
        elif largest == 5 or second_largest == 5:
            output = np.append(output,'5')
        else:
            output = np.append(output,'6')
    elif largest == 2 or second_largest == 2:
        if largest == 4 or second_largest == 4:
            output = np.append(output,'7')
        elif largest == 5 or second_largest == 5:
            output = np.append(output,'8')
        else:
            output = np.append(output,'9')
    elif largest == 3 or second_largest == 3:
        if largest == 4 or second_largest == 4:
            output = np.append(output,'*')
        elif largest == 5 or second_largest == 5:
            output = np.append(output,'0')
        else:
            output = np.append(output,'#')

for x in range(len(output)):	#Print output array
    print(output[x], end='')
print()

#Frequency Response for 697Hz BandPass filter
x, y = freqz(h_697, 1)
plt.title('Frequency Response for 697Hz')
plt.plot(x, abs(y))
plt.show()


