# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:07:03 2017

@author: Fouzi
"""

import numpy as np
import matplotlib.pyplot as plt

def perfect_sweep(N):
    
#   obtain the full length of the signal:
#   (m = M/2) where M=N is the length of one period of the sequence
   Nhalf = int(np.ceil(N/2))
   m = np.arange(Nhalf+1)
#   after computing half of the spectrum, we get the other half by flipping the
#   order & apply complex conjugate, then transform it back to the time domain.
#   the argument of the exponential term increases quadratically 
#   in the freq. domain due to the (m^2)
   ph = np.exp(-1j * 2* np.pi * m**2 / N)
   return np.fft.irfft(ph)
