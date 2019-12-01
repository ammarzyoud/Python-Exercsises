# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:07:06 2019

@author: Ammar
"""

# Exercises Day 9

# Exercise 1
#import statistics as st
#
#X = [3,1.5,4.5,6.75,2.25,5.75,2.25]
#print(st.mean(X))
#print(st.harmonic_mean(X))
#print(st.median(X))
#print(st.median_low(X))
#print(st.median_high(X))
#print(st.median_grouped(X))
#print(st.mode(X))
#print(st.pstdev(X))
#print(st.pvariance(X))
#print(st.stdev(X))
#print(st.variance(X))

#output ---------->
#3.7142857142857144
#2.8769027134348115
#3
#3
#3
#3.0
#2.25
#1.8391990270833904
#3.38265306122449
#1.9865619978819116
#3.9464285714285716

# Exercise 2
#import random
#print (random.random())
#print (random.randrange(10)) 
#print (random.choice(["Ali","Khalid","Hussam"])) 
#print (random.sample(range(1000), 10))
#print (random.choice("Orange Academy"))
#arr = [1,5,8,9,2,4]
#random.shuffle(arr)
#print (arr)
#print (random.randint(20,30))
#print (random.randrange(1000,2111,5)) 
#print ( random.uniform(10000,11000))

# Exercise 3
#import math
#print (math.pi)
#print(math.cos(200))
#print(math.sin(200))
#print(math.tan(200))
#print(math.floor(10.8))
#print(math.ceil(10.8))

# Exercise 4
from PIL import Image , ImageFilter, ImageDraw
#Q1
#img = Image.open("dubai.jpg")
#print(img.format, img.size, img.mode)
#img.show()
#output ----> JPEG (259, 194) RGB

#Q2
#image = Image.open('dubai.jpg')
#
#image_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
#image_flip.show()

#Q3
#img = Image.open("newyork.jpg")
#greyscale_image = img.convert("L")
#greyscale_image.show()

#Q4
#image = Image.open('dubai.jpg')
#cropped_image = image.crop((0,0,50,50))
#cropped_image.show()

#Q5
#img = Image.open("dubai.jpg") 
#draw = ImageDraw.Draw(img) 
#draw.line((0,0) +img.size , fill=(255,255,255))
#draw.line((0 , img.size[1] ,img.size[0],0) , fill=(255,255,255))
#draw.text((img.size[0]/2 - img.size[0]/2,img.size[0]/2 + 20) , "Ammar" ,fill=(255,255,0))
#img.show()

#Q6
#img = Image.open("dubai.jpg") 
#EDGE_ENHANCE = img.filter(ImageFilter.EDGE_ENHANCE)
#EDGE_ENHANCE.show()

#FIND_EDGES = img.filter(ImageFilter.FIND_EDGES)
#FIND_EDGES.show()

#SMOOTH = img.filter(ImageFilter.SMOOTH)
#SMOOTH.show()

#SHARPEN = img.filter(ImageFilter.SHARPEN)
#SHARPEN.show()

#Q7
#alpha = 0.5
#img1 = Image.open("dubai.jpg") 
#img2 = Image.open("newyork.jpg").resize(img1.size) 
#
#Image.blend(img1,img2,alpha).show()

#Q8
#img = Image.open("dubai.jpg") 
#blurred = img.filter(ImageFilter.BLUR)
#blurred.show()

#Q9
#img = Image.open("dubai.jpg")
#img.thumbnail((128,128))
#img.show()

#Q10
#img = Image.open("dubai.jpg")
#imageRot = img.rotate(90)
#imageRot.show()

#Q11
#img1 = Image.open('dubai.jpg')
#img2 = Image.open('newyork.jpg').resize(img1.size)
#mask = Image.open('mask.jpg')
#mask = mask.resize(img1.size)
#Image.composite(img1, img2, mask).show()
