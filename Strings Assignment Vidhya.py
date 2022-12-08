#!/usr/bin/env python
# coding: utf-8

# In[11]:


w= "Life is short"
w.lower()


# In[42]:


word = "PYTHON"
s = " "
for i in range(len(word)):
    if i%2==0:
        s +=word[i].upper()
        
    else:
        s += word[i].lower()
s
        
  


# In[44]:


word = "PYTHON"
s = " "
for i in range(len(word)):
    if i%2==0:
        s +=word[i].lower()
        
    else:
        s += word[i].upper()
s
        
  


# In[45]:


word = "PYTHON"
s = " "
for i in range(len(word)):
    if i%2==0:
        s +=word[i].lower()
        
    else:
        s += word[i].upper()
s


# In[46]:


word = "PYTHON"
s = " "
for i in range(len(word)):
    if i%2==0:
        s +=word[i].upper()
        
    else:
        s += word[i].lower()
s
        
  


# In[70]:


w = {"name":"vidhya","gender": "F", "age": 20, "phone number":100}
Biodata = print("my name is",w["name"],"my gender is",w["gender"],"My phone number is",w["phone number"])


# In[56]:


V ="S@ndhy@"
V.count("@")


# In[59]:


w = "name1.@gmail.com, name2.@gmail.com, name3.@gmail.com"
w.split("@gmail.com")


# In[64]:


w = "abcdefghijklmnopqrstuvwxyz"
d = ('a','e','i','o','u')
r = " "
for i  in w:
    if i not in d:
        r= r+i
print(r)
    


# In[69]:


str1 = "Welcome to Innomatics, innomatics awesome, isn't it?"
w = str1.lower()
r = w.count("innomatics")
print("Innomatics count is: ",r)


# In[ ]:




