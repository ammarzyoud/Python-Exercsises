# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:31:52 2019

@author: Ammar
"""

# Exercises 

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import *

# Exercise 1
print ("-----------------------------------------")
#parent = Tk()  
#svalue = StringVar()
#svalue2 = StringVar()
#def Press():
#    if svalue.get() == "Orange" and svalue2.get() == "CodingAcademy":
#        print ("Successful login")
#        parent.destroy()
#    else:
#        print ("Wrong User Name or Password")
#name = Label(parent,text = "Name").grid(row = 0, column = 0)  
#w = Entry(parent,textvariable = svalue).grid(row = 0, column = 1)  
#password = Label(parent,text = "Password").grid(row = 1, column = 0)  
#w = Entry(parent,textvariable = svalue2).grid(row = 1, column = 1)  
#submit = Button(parent, text = "Submit",command = Press).grid(row = 4, column = 0)  
#parent.mainloop()   

# Exercise 2
print ("-----------------------------------------")
#def openMessage():
#    print('Hellow,Press me again')
#    dialog_title = 'meassage'
#    dialog_text = 'This is a message'
#    text=messagebox.showinfo(dialog_title, dialog_text)
#def openChild():
#    c = Toplevel(root)
#    c.title("child 1")
#    c.geometry("200x160+230+130")
#    name = Label(c,text = "Name").grid(row = 0, column = 0)  
#    e1 = Entry(c).grid(row = 0, column = 1)  
#    password = Label(c,text = "Password").grid(row = 1, column = 0)  
#    e2 = Entry(c).grid(row = 1, column = 1)  
#    submit = Button(c, text = "Submit").grid(row = 4, column = 0)  
#    parent.mainloop()  
#
#def openChild2():
#    c = Toplevel(root)
#    c.title("child 2")
#    c.geometry('350x200')
#    txt = scrolledtext.ScrolledText(c,width=40,height=10)
#    scrollbar = Scrollbar(c)
#    txt = scrolledtext.ScrolledText(c,width=30,height=10)
#    mylist = Listbox(c, yscrollcommand = scrollbar.set )
#    for line in range(100):
#        mylist.insert(END, "This is line number " + str(line))
#    mylist.pack( side = LEFT, fill = BOTH )
#    txt.grid(column=0,row=0)
#    
#root = Tk()
#root.title("Root Window")
#
#Button(root,text="open Message",command = openMessage).grid()
#Button(root,text="open child 1",command = openChild).grid()
#Button(root,text="open child 2",command = openChild2).grid()
#root.mainloop()   
    
# Exercise 3
print ("-----------------------------------------")
#def getColor():
#    color = askcolor() 
#    print(color[1])
#    mycolor.configure(background=color[1])
#
#mycolor = Tk()
#mycolor.geometry("100x100") 
#Button(text='Select Color', command=getColor).pack()
#mycolor.eval('tk::PlaceWindow . center')
#
#mycolor.mainloop()
