#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import datasets


# #1 Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in acomma-separated sequence on a single line.
# 

# In[3]:


nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


# #2 Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[4]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# #3 Write a Python program to find the volume of a sphere with diameter 12 cm

# In[5]:


pi = 22/7
r= 12
V= 4/3*pi* r**3
print('The volume of the sphere is: ',V)


# #4 Create the below pattern using nested for loop in Python

# In[8]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	


# #5 Write a Python program to reverse a word after accepting the input from the user

# In[4]:


word = input("Input a word to reverse: ")
b = word[::-1]
print (b)


# In[ ]:





# #6 Write a Python Program to print the given string in the format specified in the sample output.
# 
# 

# WE, THE PEOPLE OF INDIA,
# having solemnly resolved to constitute India into a SOVEREIGN, !
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# and to secure to all its citizens
# 

# In[27]:


a =('WE, THE PEOPLE OF INDIA,  \n\thaving solemnly resolved to constitute India into SOVEREIGN!, \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens')


# In[28]:


a.expandtabs()
print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




