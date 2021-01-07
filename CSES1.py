#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input())
l = [n]
while n!=1:
    if n%2==0:
        n = n//2
        l.append(n)
    else:
        n = (3*n) + 1
        l.append(n)
print(*l)        


# In[ ]:




