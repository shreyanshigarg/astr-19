#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a Jupyter notebook, import matplotlib. Write cells that create an array x ranging from [0,1] in 100 steps
# and that defines functions that return sin(x) and cos(x).  
# In a new cell use to create a multipanel plot (1 row, 2 columns), plotting sin(x) vs. x 
# in the left panel and cos(x) vs. x in the right panel. Label the panels with sin(x) and cos(x), and save the 
# figure as a PDF.


# In[9]:


import matplotlib.pyplot as plt
import numpy as np


# In[10]:


x = np.arange(0,1,0.01)


# In[11]:


def sin_x():
    sinx = np.sin(x)
    return sinx
def cos_x():
    cosx = np.cos(x)
    return cosx


# In[20]:


f, axarr = plt.subplots(1,2)

axarr[0].plot(x, sin_x())
axarr[0].set_xlabel('x')
axarr[0].set_ylabel('sin(x)')
axarr[0].set_title(r'$\sin(x)$')


axarr[1].plot(x, cos_x())
axarr[1].set_xlabel('x')
axarr[1].set_ylabel('cos(x)')
axarr[1].set_title(r'$\cos(x)$')

f.subplots_adjust(wspace=0.4)

plt.savefig('trig.pdf', bbox_inches = 'tight', dpi = 600)


# In[ ]:




