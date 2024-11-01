#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a Jupyter notebook, import matplotlib. On the numpy website, read about the random number distributions
# available for pulling random variates.  Select your favorite distribution (other than uniform) and pull
# 1000 random numbers from that distribution. Histogram the random numbers into 100 bins, and plot the histogram. 
# Label your axes and save the figure as a PDF.


# In[21]:


import matplotlib.pyplot as plt
import numpy as np


# In[32]:


rng = np.random.default_rng()
x = rng.normal(size = 1000)


# In[30]:


bins = 100
plt.hist(x, bins, alpha=0.6, color='purple', edgecolor = 'black')
plt.xlabel("x")
plt.ylabel("Number per bin")
plt.title("Random numbers histogram")
plt.savefig('hist_random.pdf', bbox_inches = 'tight', dpi = 600)


# In[ ]:





# In[ ]:




