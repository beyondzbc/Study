#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[10]:


columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year','origin','car name']
cars=pd.read_table('D:/pydata/auto_mpg.data',delim_whitespace=True,names=columns)
#delim_whitespace指定是否将空格作为sep


# In[12]:


cars.head()


# In[13]:


fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
cars.plot('weight','mpg',kind='scatter',ax=ax1)
cars.plot('acceleration','mpg',kind='scatter',ax=ax2)

#图一为  车重/油量，图二为  加速度/油量


# class sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
# 参数: 
# fit_intercept : 布尔型,可选.是否计算模型的截距.要是设置为False的话,就不会计算截距了.(表明数据已经中心化了.) 
# normalize : 布尔型,可选,默认是False.如果是True的话,X就会在回归之前标准化.当fit_intercept被设置为False后,这个参数会被忽略. 
# copy_X : 布尔型,可选,默认是True.表示X会被拷贝.否则的话,X可能被重写改变. 
# n_jobs : int类型,可选,默认是1. 表示计算的时候使用的多个线程.如果设置为-1的话,那么所有CPU都会被使用到.

# In[16]:


from sklearn.linear_model import LinearRegression
lr=LinearRegression(fit_intercept=True)
lr.fit(cars[['weight']],cars['mpg'])
predictions=lr.predict(cars[['weight']])
print(predictions[0:5])
print(cars['mpg'][0:5])

plt.scatter(cars['weight'],cars['mpg'],c='r')
plt.scatter(cars['weight'],predictions,c='y')


# In[19]:


#算出均方误差
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(cars['mpg'],predictions)
print(mse)
#根号均方误差
rmse=mse**0.5
print(rmse)


# In[ ]:




