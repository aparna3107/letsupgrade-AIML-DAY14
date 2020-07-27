# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:19:35 2020

@author: Aparna S Nair
"""
import numpy as np 
# 1. Create a 3x3x3 array with random values
x = np.random.random((3,3,3))
print(" Create a 3x3x3 array with random values ")
print(x) 
 
# 2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
y = np.zeros((5,5),int)
y[1,0]=1
y[2,1]=2
y[3,2]=3
y[4,3]=4
print(y)

# 3.Create a 8x8 matrix and fill it with a checkerboard pattern
z=np.zeros((5,5),int)
z[1::2, ::2] = 1
z[::2, 1::2] = 1
print("8x8 matrix and fill it with a checkerboard pattern :")
print(z)

# 4. Normalize a 5x5 random matrix
w= np.random.random((5,5))
print("Original Array:")
print(w)
wmax, wmin = w.max(), w.min()
w = (w - wmin)/(wmax - wmin)
print("After normalization:")
print(w)

# 5.  How to find common values between two arrays?
array1 = np.array([1, 2, 3, 4, 5])
print("Array1: ",array1)
array2 = [3, 6, 4, 0, 5]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))

# 6.How to get the dates of yesterday, today and tomorrow?
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday: ",yesterday)
today  = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)

# 7. Consider two random array A and B, check if they are equal
A= np.random.randint(0,2,6)
print("First array:")
print(A)
B = np.random.randint(0,2,6)
print("Second array:")
print(B)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(A,B)
print(array_equal)

# 8.Create random vector of size 10 and replace the maximum value by 0 
g = np.random.random(10)
print("Original array:")
print(g)
g[g.argmax()] = 0
print("Maximum value replaced by 0:")
print(g)

# 9. How to print all the values of an array?
C=np.array([5,4,3,2,1,0])
print('all elements in array are:')
print(C)
print(type(C))
print(C.shape)

# 10.Subtract the mean of each row of a matrix
print("Original matrix:")
X = np.random.rand(5, 10)
print(X)
print(" Subtract the mean of each row of the said matrix: ")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)

# 11.Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)?
arr1 = np.array([3, 2, 1])
arr2=np.ones_like(arr1)
print ("given array : ", arr1)
out_arr = np.add(arr1, arr2)  
print ("added array : ", out_arr) 

# 12.How to get the diagonal of a dot product?

f = np.array([[1,2],[3,4]]) 
d = np.array([[11,12],[13,14]]) 
T=np.dot(f,d)
print('dot product is: ')
print(T)
print("diagonal of dot product is: ")
print(T.diagonal())

# 13.How to find the most frequent value in an array?
h = np.array([0, 10, 40,0,5,4,0,2,7,0,2])
print("Original array:")
print(h)
print("Most frequent value in the above array:")
print(np.bincount(h).argmax())

# 14.How to get the n largest values of an array
k = np.arange(10)
print("Original array:")
print(k)
np.random.shuffle(k)
n = 1
print (k[np.argsort(k)[-n:]])

# 15.How to create a record array from a regular array?
a1=np.array([1,2,3,4])
a2=np.array(['Red','Green','White','Orange'])
a3=np.array([12.20,15,20,40])
result= np.core.records.fromarrays([a1, a2, a3],names='a,b,c')
print(result[0])
print(result[1])
print(result[2])
 

