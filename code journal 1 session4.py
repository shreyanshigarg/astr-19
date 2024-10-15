#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a Python program that declares a class describing your favorite animal.
# Have the data members of the class represent the following physical parameters of the animal:
# length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool),
# is it furry? (bool). Write an initialization function that sets the values of the data members when 
# an instance of the class is created. Write a member function of the class to print out and describe the data
# members representing the physical characteristics of the animal.


# In[10]:


class Animal:
    # Initialization function (constructor)
    def __init__(self, arm_length, leg_length, num_eyes, tail, furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.tail = 'Yes' if tail else 'No'
        self.furry = 'Yes' if furry else 'No'
        
    def describe(self):
        print("Animal description:")
        print(f"Arm length: {self.arm_length} meters")
        print(f"Leg length: {self.leg_length} meters")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Does it have a tail? {self.tail}")
        print(f"Is it furry? {self.furry}")
        
def main():
    my_favorite_animal = Animal(0.5, 0.7, 2, False, False)
    
    # Call the describe method to print the animal's characteristics
    my_favorite_animal.describe()


if __name__ == "__main__":
    main()
        


# In[ ]:




