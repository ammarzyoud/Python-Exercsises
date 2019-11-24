# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:05:54 2019

@author: Ammar
"""

# Exercises

# Exercise 1
#o = lambda x = 1, y = 2, z = 3 : x+y+z
#print(o())
#print(o(10))
#print(o(10,20)) 
#output ----> 6 15 33

# Exercise 2
#def multiplier(a,b):
#   for n in a,b:
#       multi = a * b
#   print("Result :",multi)
#multiplier(3,5)

# Exercise 3
#multi = lambda a,b : a * b
#print(multi(2,5))

# Exercise 4
#number_list = range(-5,5)
#negNums = list(filter(lambda x: (x < 0), number_list)) 
#print("Negative numbers :",negNums) output ------> [-5, -4, -3, -2, -1]

# Exercise 5
#x = lambda a,b,c : a+b+c
#print (x(5,6,2))

# Exercise 6
#x = ("Joi","Monica","Ross")
#y = ("Chandler","Phoep")
#z = ("david","rachel","Courty")
#result = list(zip(x,y,z))
#print(result) output ------> [('Joi', 'Chandler', 'david'), ('Monica', 'Phoep', 'rachel')]

# Exercise 7
#coin =('Bitcoin','Ether','Ripple','Litecoin')
#code=('BTC','ETH','XRP','LTC')
#d=dict(zip(coin,code))
#print(d)
#output ------>
#{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

# Exercise 8
#def fun(variable):
#    letters = ['a','e','i','o','u']
#    if(variable in letters):
#        return True
#    else:
#        return False
#    
#sequence =['g','j','e','j','k','o','p','r']
#filtered = list(filter(fun, sequence))
#print(filtered)
#output ---------> ['e', 'o']

# Exercise 9
#x=list(map(int,input("Enter a multitple a value:").split()))
#print("List of students:",x) output ---->  [1, 20, 10]

# Exercise 10
#def newfunc(a):
#    return a*a
#x =list(map(newfunc,(1,2,3,4)))
#print(x) output -----> [1, 4, 9, 16]

# Exercise 11 
#def fun(a,b):
#    return a+b
#a = list(map(fun,[2,4,5],[1,2,3,4,5]))
#print(a) output ----> [3, 6, 8]

# Exercise 12
#c = map(lambda x: x+x , filter(lambda x: (x >= 3),(1,2,3,4)))
#print(list(c)) output ----> [6, 8]

# Exercise 13
#c = filter(lambda x: (x >= 3) , map(lambda x: x+x,(1,2,3,4)))
#print(list(c)) output ----> [4, 6, 8]

# Exercise 14
#from functools import reduce 
#List = [5,2,7,9,8,6]
#reduced = reduce(lambda a,b: a if a < b else b, List) 
#print(reduced) output ----> 2

# Exercise 15
#numbers = [1,2,3]
#letters = ["a","b","c"]
#results = list(zip(numbers, letters))
#print(results) output ----> [(1, 'a'), (2, 'b'), (3, 'c')]








