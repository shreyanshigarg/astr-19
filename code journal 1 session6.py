#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a Jupyter Notebook where, in separate cells, you define functions that return sin(x) and cos(x).
# Use Markdown cells to comment your Notebook, and describe what each function does. 
# Create a third Python cell that will tabulate sin(x) and cos(x) using these previously defined functions vs. x,
# where x is tabulated between 0 and 2pi with a thousand entries. 
# Write a fourth Python cell that will use a for loop to print out the first 10 values of
# x, sin(x), and cos(x) in columns.


# In[2]:



import numpy as np
from astropy.table import Table


# In[51]:


x_lin = np.linspace(0, 2*np.pi, 1000)
x = np.round(x_lin, 5)
def sin():
    sinx = np.sin(x)
    sinx = np.round(sinx, 5)
    return sinx


# In[55]:


def cos():
    cosx = np.cos(x)
    cosx = np.round(cosx, 5)
    return cosx


# In[56]:


table_sin = Table([x,sin(), cos()],names=['x','sin(x)', 'cos(x)'])
# table_cos = Table([x,cos()],names=['x','cos(x)'])


# In[57]:


for i in range(10):
    print (table_sin[i])    


# In[ ]:




