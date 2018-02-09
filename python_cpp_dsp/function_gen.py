import numpy as np
import matplotlib.pyplot as plt
import tkinter

freq = 1000
length= 0.01
sample_rate = 44000

x = np.linspace(0,length,length*sample_rate)

y1 = np.sin(2*np.pi*freq*x)
y2 = np.sin(2*np.pi*2*freq*x)
y3 = np.sin(2*np.pi*1.5*freq*x)

print(length*sample_rate)

noise = np.random.normal(0,0.5,int(length*sample_rate))

signal = y1+y2+y3+noise

plt.plot(x,signal)
plt.show()
