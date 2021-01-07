#!/usr/bin/env python
# coding: utf-8

# In[8]:


def compute(s):
    if len(s)==0:
        return
    if len(s)==1:
        return 1
    ans = 1
    temp = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            temp = temp + 1
        else:
            ans = max(ans,temp)
            temp = 1
    ans = max(ans,temp)
    return ans

s = input()
print(compute(s))

