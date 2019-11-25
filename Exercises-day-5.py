# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:44:52 2019

@author: Ammar
"""

# Exercise 

# Exercise ------------->
class Employees(object):
    def __init__(self,number,name,address,salary,jobTitle):
        self.number = int(number)
        self.__name = str(name)
        self.__address = str(address)
        self.__salary = float(salary)
        self.__jobTitle = str(jobTitle)
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getSalary(self):
        return self.__salary
    def getJobTitle(self):
        return self.__jobTitle
    def setAddress(self,newVal):
        self.__address = newVal
        return print (self.getName(),"New Address : ",self.__address)
    def printEmp(self):
        print ("Employee Number :",self.number)
        print ("Name :",self.getName())
        print ("Address :",self.getAddress())
        print ("Salary :",self.getSalary())
        print ("Job Title :",self.getJobTitle())
    def printEmpFormat2(self):
        print ("Employee Number :",self.number,"Name :",self.getName(),"Address :",self.getAddress(),"Salary :",self.getSalary(),"Job Title :",self.getJobTitle())
#    def __del__(self):
#        print (self.__name , "has been deleted")
        
Employee1 = Employees(1,"Mohmmad khalid","amman,jordan",500,"consultant")
Employee2 = Employees(2,"Hala rana","aqaba,jordan",750,"Manager")

# Print the Employee from the class function
#print (Employee1.printEmp())
# Print the Employee from the class function seconde format
#print (Employee1.printEmpFormat2())

# Set New Address
#print (Employee1.setAddress("USA"))

# Delete the employee from the class
#del Employee1

#-------------------------------------------------------------------