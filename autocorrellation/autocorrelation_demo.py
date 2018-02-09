#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
length = 1
f1 = 200
f2 = 300

Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector

y = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)
noise = 0.2*np.random.rand(Fs*length)
y = y + noise

corr = np.correlate(y,y,"same")

plt.plot(corr)
plt.show()

