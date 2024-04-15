# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:38:01 2024

@author: mdubo
"""

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def f(x): return x**2 #defines function

print(f'{quad(f, 0, 2)[0]}  is the result of integrating x^2 from 0 to 2.\n'); #integrates function

def g(x): return np.exp(-(x**2)/2) #defines function

xvals = np.linspace(0, 5, 6) #defines range over which we will integrate function
fvals = np.zeros(len(xvals)) #empty variable we will store integral data in

for i in range(len(xvals)):
    fvals[i] = quad(g, 0, xvals[i])[0] #for each value of x, what is the value of the integral of g?
    
print(f'{quad(g,0,5)[0]} is the result of integrating the function from 0 to 5.\n') #calculates integral
plt.plot(xvals,fvals, 'purple') #plots integral
    
print(f'{quad(g, -np.inf, np.inf)[0]} is the result of integrating the function from negative infinity to infinity, and {np.sqrt(2*np.pi)} is the square root of 2*pi.') #calculates integral and compares to expected value

