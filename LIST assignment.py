#!/usr/bin/env python
# coding: utf-8

# # LIST assignment 

# In[2]:


# Sum of all the numbers
s = [1,2,3,4,5,6]
v = 0
for i in s:
    v= v+i
v
    


# In[3]:


# multiplication of all the numbers
d = [1,2,3,4,5,6]
l = 1
for i in d:
    l = l*i
l
    


# In[12]:


s = list(input("enter list of nums: "))
e = list(input("enter list of nums: "))
def stuff(s,e):
    if i in s:
        print(True)
    else:
        print("not present")
stuff(s,e)


# In[16]:


c1 =['red','white','blue','yellow']
c2 =['red','black','orange']
for i in c1:
    if i  in c2 :
        c1.remove(i)
c1        


# In[17]:


l1=["red", "orange", "green", "blue", "white"] 
l2=["black", "yellow", "green", "blue"]
l= []
for i in l2:
    if i not in l1:
        l.append(i)
l


# In[ ]:




