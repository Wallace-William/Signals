#William Wallace 
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

pulse0 = np.ones(10)				# Bit 0
pulse0 = pulse0/np.linalg.norm(pulse0)

pulse1 =  np.append(np.ones(5), -1*np.ones(5))	# Bit 1
pulse1 = pulse1/np.linalg.norm(pulse1)

with open('data-communications.csv') as f:	# Read file to find number of data points
    file_content = f.read()
num_data = file_content.count('.')
num_data = int(num_data/10)			# Separate into 10 data point chunks

csv = np.genfromtxt('data-communications.csv',delimiter=",")	# Read csv, separate based on ','

csv = np.split(csv, num_data)			# Split based on number of data points found in file read

answer = -1					# Default answer value
	
bits = []					# Array of bits for ascii conversion
for i in range(0, num_data):			
    array = csv[i]
									# Given equations to produce numbers to compare to bit 0 and 1
    a = (np.dot(array, pulse0))/(LA.norm(array) * LA.norm(pulse0))	# Use equation to compare to pulse 0
    b = np.dot(array, pulse1)/(LA.norm(array) * LA.norm(pulse1))	# Compare with pulse 1

    compare_a = 1-a							# Calculate difference
    compare_b = 1-b

    if compare_a > compare_b: 						# Assign bit 1 or 0 based on how close value is to 1
        answer = 1
    else:
        answer = 0

    bits.append(answer)							# Append bit to bit array for later conversion

print(bytearray(np.packbits(bits)).decode().strip("\x00"))		# Convert by byte to ascii then print result

