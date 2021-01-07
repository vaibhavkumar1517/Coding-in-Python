#!/usr/bin/env python
# coding: utf-8

# In[12]:


def compute(arr):
    if len(arr)==1:
        return 0
    ans = 0
    mx = arr[0]
    for i in range(1,len(arr)): 
        if arr[i]>mx:
            mx = arr[i]
        ans = ans + (mx-arr[i])
               
    return ans    
        
n = int(input())
arr = list(map(int,input().split()))
print(compute(arr))


# %%
