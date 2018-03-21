# Jonathan Metzger
# CS453x Jacob Whitehill
# March 20th 2018

import numpy as np

# arrays
A = np.array([[3,5],[6,2]])
B = np.array([[2,3],[7,5]])
C = np.array([[5,3],[13,5]])

x = np.array([[5],[6]])
y = np.array([[4],[8]])

# scalars
alpha = 2
c = 0
d = 4

k = 5

## row
i = 0
## column
j = 1

def problem1 (A, B):
	print "Problem 1"
	print A + B

def problem2 (A, B, C):
	print "Problem 2"
	print np.dot(A,B) - C

def problem3 (A, B, C):
	print "Problem 3"
	print A * B + np.transpose(C)

def problem4 (x, y):
	print "Problem 4"
	print np.dot(np.transpose(x), y)

def problem5 (A):
	print "Problem 5"
	print np.zeros_like(A)

def problem6 (A):
	print "Problem 6"
	print np.ones(A.shape[1])

def problem7 (A):
	print "Problem 7"
	print np.linalg.inv(A)

def problem8 (A, alpha):
	print "Problem 8"
	I = np.eye(A.shape[0])
	print A + alpha * I

def problem9 (A, i, j):
	print "Problem 9"
	print A[i,j]

def problem10 (A, i):
	print "Problem 10"
	print np.sum(A[i])

def problem11 (A, c, d):
	print "Problem 11"
	val =  A[(A >= c) * (A <= d)]
	print np.mean(val)

def problem12 (A, k):
	print "Problem 12"
	eigvalues,arr = np.linalg.eig(A)
	print np.dot(eigvalues,k)

def problem13 (A, x):
	print "Problem 13"
	A_inv = np.linalg.inv(A)
	print np.linalg.solve(A_inv, x)

def problem14 (A, x):
	print "Problem 14"
	A_inv = np.linalg.inv(A)
	A_tra = np.transpose(A_inv)
	x_tra = np.transpose(x)
	final = np.transpose(np.dot(x_tra, A_tra))
	print final
	
print("\nJonathan Metzger\nHomework1a\nCS453x Machine Learning\n")
problem1(A,B)
print
problem2(A,B,C)
print
problem3(A,B,C)
print
problem4(x,y)
print
problem5(A)
print
problem6(A)
print
problem7(A)
print
problem8 (A, alpha)
print
problem9 (A, i, j)
print
problem10 (A, i)
print
problem11 (A, c, d)
print
problem12 (A, k)
print
problem13 (A, x)
print
problem14 (A, x)
print