#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Write a Python that prints the sum of two floating point numbers, the difference between
# two integers, and the product of a floating point number and an integer. 
# In each case, have the program print out the data type of the resulting answer.


# In[8]:


num1 = float(4.5)
num2 = float(5.3)
integer1 = int(6)
integer2 = int(10)
sum_float = num1 + num2
diff = integer2-integer1
product = integer2*num1

print(f"Sum of two floating point numbers:{sum_float, type(sum_float)}")
print(f"Diffence between two inetgers:{diff, type(diff)}")
print(f"Product of two floating point numbers:{product, type(product)}")


# In[ ]:




