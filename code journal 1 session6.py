#!/usr/bin/env python
# coding: utf-8

# In[130]:


# Create a Jupyter Notebook where, in separate cells, you define functions that return sin(x) and cos(x).
# Use Markdown cells to comment your Notebook, and describe what each function does. 
# Create a third Python cell that will tabulate sin(x) and cos(x) using these previously defined functions vs. x,
# where x is tabulated between 0 and 2pi with a thousand entries. 
# Write a fourth Python cell that will use a for loop to print out the first 10 values of
# x, sin(x), and cos(x) in columns.


# Importing libraries

# In[136]:


import numpy as np
from astropy.table import Table


# Define x and sin(x) and round them off to 5 digits so the table does not look distorted

# In[137]:


x_lin = np.linspace(0, 2*np.pi, 1000)
x = np.round(x_lin, 5)
def sin():
    sinx = np.sin(x)
    sinx = np.round(sinx, 5)
    return sinx


# Define cos(x) and round it off too

# In[138]:


def cos():
    cosx = np.cos(x)
    cosx = np.round(cosx, 5)
    return cosx


# Tabulate sin(x) and cos(x) using the previously defined functions vs. x using the function "Table" in the same table. 

# In[139]:


table_main = Table([x,sin(), cos()],names=['x','sin(x)', 'cos(x)'])


# Use the for loop to print only the first 10 values

# In[140]:


print(f"x               sin(x)          cos(x)")
for i in range(10):
    x = table_main['x'][i]
    sin_x = table_main['sin(x)'][i]
    cos_x = table_main['cos(x)'][i]
    print(f"{x:<15.5f} {sin_x:<15.5f} {cos_x:<15.5f}")


# In[ ]:




