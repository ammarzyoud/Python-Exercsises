# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:30:02 2019

@author: Ammar
"""

# Python Exercises Day-7

import matplotlib.pyplot as plt
import numpy as np

# Exercise 1
a=np.zeros((1,10))
b=np.ones((1,10))
c=np.ones((1,10))*5
print(a,"\n",b,"\n",c)
print("--------------------------------------------------------")

# Exercise 2
arr = np.arange(30,71)
print(arr)
print("--------------------------------------------------------")

# Exercise 3
arr = np.arange(30,71,2)
print(arr)
print("--------------------------------------------------------")

# Exercise 4
arr = np.eye(3)
print(arr)
print("--------------------------------------------------------")

# Exercise 5
randNum=np.random.normal(0,1)
print(randNum)
print("--------------------------------------------------------")

# Exercise 6
arr = np.arange(10,22).reshape((3,4))
for x in arr:
    print(x)
print("--------------------------------------------------------")

# Exercise 7
x = np.arange(21)
print(x)
x[(x>=9)&(x<=15)]*=-1
print(x)
print("--------------------------------------------------------")

# Exercise 8
x = [1,8,3,5]
y = np.random.randint(0,11,4)
print(x*y)
print("--------------------------------------------------------")

# Exercise 9
x = np.arange(10,22).reshape((3, 4))
print(x)
print(x.shape)
print("--------------------------------------------------------")

# Exercise 10
x = np.random.random((3, 3, 3))
print(x)
print("--------------------------------------------------------")

# Exercise 11
a = np.array([9,-1,2,5])
b = np.array([1,-6,0,10])
c = np.array([[1,8,2,5],[3,1,7,9]])
print("a-b: ",a-b)
print("a*b: ",a*b) 
print("a.dot(b): ",a.dot(b)) 
print("a*2: ",a*2) 
print("np.sin(a): ",np.sin(a)) 
print("a<3: ",a<3) 
print("a.sum(): ",a.sum()) 
print("a.sum(axis=0): ",a.sum(axis=0)) 
print("c.sum(): ",c.sum()) 
print("c.sum(axis=0): ",c.sum(axis=0)) 
print("a.min(): ",a.min()) 
print("a.max(): ",a.max()) 
print("a.mean(): ",a.mean()) 
print("a average(): ",np.average(a)) 
print("a median(): ",np.median(a)) 
print("a std(): ",np.std(a)) 
print("a var(): ",np.var(a)) 
print("c.cumsum(): ",c.cumsum()) 
print("a[1:2] :  ",a[1:2]) 
print("a[2:] :  ",a[2:]) 
print("c[-1] :  ",c[-1])
print("--------------------------------------------------------")

# Exercise 12
X = range(1, 50)
Y = [value * 3 for value in X]
print(*range(1,50)) 
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()
print("--------------------------------------------------------")

# Exercise 13
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.legend()
plt.show()
print("--------------------------------------------------------")

# Exercise 14
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
print("--------------------------------------------------------")

# Exercise 15
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.show()