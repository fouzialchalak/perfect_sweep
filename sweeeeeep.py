# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:07:03 2017

@author: Fouzi
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sf
 


def perfectsweep(fs, N):

    # intialization
    isEven = (N % 2 == 0)
    Nhalf = int(np.ceil((N+1) / 2))
    ph = np.zeros(N)

#    groupDelay = np.arange(Nhalf) / N / (fs / 2)

#    deltaOmega = 2 * np.pi * fs / N
#    a = np.arange(1, Nhalf)
#    ph[:Nhalf] = -groupDelay * (deltaOmega * np.arange(Nhalf)) / 2
    ph[:Nhalf] = -2 * np.pi / N * np.arange(Nhalf)**2
#    a =  np.multiply((deltaOmega * np.arange(len(groupDelay)-1)), - groupDelay)
    # ph(arange(1,Nhalf)) = np.divide(a,2)

    if isEven:
        ph[Nhalf:] = -np.flipud(ph[1:Nhalf-1])
    else:
        ph[Nhalf:] = -np.flipud(ph[1:Nhalf])

    c = np.exp(1j * ph)
    s = np.real(np.fft.ifft(c))
    return s / np.max(abs(s))

N = 32
p = perfectsweep(44100, 32)
acf = np.fft.irfft(np.fft.rfft(p)*np.fft.rfft(np.roll(p[::-1], 1)), n=N)
plt.plot(acf)
#sf.play(p)
