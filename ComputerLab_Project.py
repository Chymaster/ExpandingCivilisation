###Numpy and Matplotlib environment required###

##expanding_seq(x,a) is an operation follows such:
#x(n+1) = a*x(n)*(1-x(n))
#The function intakes x(n) and a
#returns x(n+1)


#random number generator library and NumPy
import random
import numpy as np
import matplotlib as mplot

#Returns x(n+1)
def expanding_seq(x,a):
    x_ = a*x*(1-x)
    return x_


#Question 1:
#Returns the convergence point of the sequence given x, a and n
def convergent_point(a,x_init,n):
    #assign x to the initial condition
    x = x_init
    #for loop repeat n times
    for i in range(n):
        x = expanding_seq(x,a)
    return a,x

temp = [convergent_point(1.,random.random(),100)]
print (temp)
#Question 2
#An array that saves all recorded values of (a) and (converging x)
an_array = []
an_array.append(temp)


#Question 3 
 

#Function intakes a, sample_size and n
#returns list consist of elements (a,x_), where x* is convergence point
def convergent_point_list(a,sample_size,n): #!!!*n might not be taken!!!
    #List of x convergence points
    x_conv_list = []
    #np.random.random_sample(sample_size).tolist() function
    #returns a list of random samples of initial condition between 0 and 1
    #with sample size of sample_size
    for x_init in np.random.random_sample(sample_size).tolist():
        x_conv_list.append([convergent_point(a,x_init,n)])
    return x_conv_list

#Question 4




            
