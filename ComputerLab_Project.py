#random number generator library and NumPy
import random
import numpy as np
import matplotlib as mplot

#Returns x(n+1)
def expanding_seq(x,a):
    x = a*x*(1-x)
    return x

#Returns the convergence point of the sequence given x0 and a, n is optional
#It is assumed the sequence converges at n=100, so default n = 100
def convergent_point(x_init,a,*given_n):
    #Default n = 100 if no value given
    try:
        n = int(given_n)
    except TypeError:
        n = 100
    x = x_init
    #for loop repeat 100 times
    for i in range(n):
        x = expanding_seq(x,a)
    return a,x



#An array that saves all recorded values of (a) and (converging x)
conv_record = []


