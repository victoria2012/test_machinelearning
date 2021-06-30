#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[4]:


favorite_load = pickle.load(open('./saves/favorite_save.pkl','rb'))
print(favorite_load)


# In[6]:


print(type(favorite_load))          # 피클은 원래 저장하고 있었던 데이터의 성격을 그대로 가지고 있다.


# In[7]:


print(favorite_load['tiger'])


# In[10]:


autompglr = pickle.load(open('./saves/autompglr.pkl','rb'))
print(autompglr)


# In[11]:


print(type(autompglr))


# In[12]:

# input from outside
a = 3504.0
b = 8
import numpy as np
pre = np.array([[a,b]])
print(autompglr.predict(pre))

print(autompglr.predict([[3504.0,8]]))


# In[ ]:




