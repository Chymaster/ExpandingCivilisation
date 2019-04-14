###Numpy and Matplotlib environment required###

##expanding_seq(x,a) is an operation follows such:
#x(n+1) = a*x(n)*(1-x(n))
#The function intakes x(n) and a
#returns x(n+1)


#random number generator library and NumPy
import random
import numpy as np
import matplotlib.pyplot as plt

#The main function that intakes x(n) and a, and returns x(n+1)
def expanding_seq(x,a):
    x_1 = a*x*(1-x)
    return x_1


#Question 1:
#Returns the convergence point of the sequence given x, a and n
def convergent_point(a,x_init,n):
    #assign x to the initial condition
    x = x_init
    #for loop repeat n times
    for i in range(n):
        x = expanding_seq(x,a)
    return [a,x]
#temp to be found by function convergent_point(a,x_init,n)
#print (temp)


#Question 2
#An array that saves all recorded values of (a) and (converging x)
an_array = []
an_array.append(temp)
del temp

#Question 3 
 
#Function intakes a, x_init_size and n
#returns list consist of elements (a,x_), where x* is convergence point
def convergent_point_list(a,x_init_size,n): 
    #List of x convergence points
    x_conv_list = []
    for x_init in np.random.random_sample(x_init_size).tolist():#repeat with (sample_size) number of non_repeated random value
        x_conv_list.append(convergent_point(a,x_init,n))
    return x_conv_list

#Question 4

temp = []
#the line gives a random sample size of 2000 in the interval [1.5,4] in numerical order
for a in sorted((np.random.sample(2000)*2.5+1.5).tolist()):
    #a temporary variable is used to collect the data list
    temp += convergent_point_list(a,50,100)
del temp
#print (another_NumPy_array[:50])

#Question 5:


            
