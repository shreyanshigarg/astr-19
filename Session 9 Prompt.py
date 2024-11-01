#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a Jupyter notebook, import matplotlib. Use numpy to pull 1000 random numbers distributed 
# uniformly between [0,1]. Histogram the random numbers into 100 bins, and plot the histogram. 
# Label your axes and save the figure as a PDF.


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[21]:


rng = np.random.default_rng()
x = rng.uniform(0,1,1000)


# In[18]:


bins = 100
plt.hist(x, bins, alpha=0.6, color='purple', edgecolor = 'black')
plt.xlabel("x")
plt.ylabel("Number per bin")
plt.title("Uniformly distributed random numbers histogram")
plt.savefig('hist_uniform.pdf', bbox_inches = 'tight', dpi = 600)


# In[ ]:





# In[ ]:




