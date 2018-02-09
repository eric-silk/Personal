#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def square_wave_coeff(harmonic):
    return 1/(2*harmonic - 1)

def square_wave_gen(time_series, freq=1, harmonics=1):
    if freq <= 0:
        print("Frequency of 0 or less is not valid!")

    y = 0
    
    for i in range(1,harmonics+1):
        print(i)
        y_tmp = None
        y_tmp = (4/np.pi)*np.sin(2*np.pi*freq*(2*i-1)*time_series)
        coeff = square_wave_coeff(i)
        y_tmp = y_tmp * coeff
        y = y + y_tmp

    return y


def main():
    max_harmonics_to_gen = 5
    sample_rate = 2**(max_harmonics_to_gen+1)
    print(2**max_harmonics_to_gen)
    print(sample_rate)
    time_min = -0.5
    time_max = 1.5
    frequency = 2  # To show both rising and falling edges within 1 second

    num_samples = (time_max - time_min) * sample_rate

    t = np.linspace(time_min, time_max, num_samples)
    #y1 = square_wave_gen(t, harmonics=1)
    #y2 = square_wave_gen(t, harmonics=2)
    #y4 = square_wave_gen(t, harmonics=4)
    #y5 = square_wave_gen(t, harmonics=15)
    y6 = square_wave_gen(t, harmonics=max_harmonics_to_gen)
    
    print(y6.max())
    plt.plot(t,y6)
    plt.show()

if __name__ == "__main__":
    main()
