#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Create a Jupyter notebook, import matplotlib. Write cells that create an array x ranging from [0,1] in 100 steps 
# and that defines a function that returns exp(x). 
# In a new cell use the function to set y=exp(x), and then plot x vs. y. 
# Label the x-axis as “Time [milliseconds]” and the y-axis as “Awesomeness”. Save the figure as a PDF.  


# In[15]:


import matplotlib.pyplot as plt
import numpy as np


# In[19]:


x = np.arange(0,1,0.01)


# In[17]:


def exp_x():
    expx = np.exp(x)
    return expx


# In[18]:


y = exp_x()
plt.plot(x,y)
plt.xlabel('Time [milliseconds]')
plt.ylabel('Awesomeness')
plt.savefig('exp(x).pdf', bbox_inches = 'tight', dpi = 600)


# In[ ]:




