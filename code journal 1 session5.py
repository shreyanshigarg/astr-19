#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a Python program that writes out a table of the function sin(x) vs. x, 
# where x is tabulated between 0 and 2pi with a thousand entries. 
# Follow the basic Python program structure, including a main program function.


# In[76]:


from tabulate import tabulate
import numpy as np
from astropy.table import Table


# In[123]:


x_lin = np.linspace(0, 2*np.pi, 1000)
x = np.round(x, 6)
def sin_table():
    sinx = np.sin(x)
    table = Table([x,sinx],names=['x','sin(x)'])
    
def main():
    table()

if __name__ == "__main__":
    main()

