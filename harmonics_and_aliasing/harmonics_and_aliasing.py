#! /usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

Fs = 2000.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector

ff = 750;   # frequency of the signal
y = np.sin(2*np.pi*ff*t)
y2 = y**2

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
m = n/2
m = int(m)
frq = frq[range(m)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(m)]
Y2 = np.fft.fft(y2)/n # fft computing and normalization
Y2 = Y2[range(m)]

plt.stem(frq,abs(Y2))
plt.show()
