#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year','origin','car name']
cars=pd.read_table('D:/pydata/auto_mpg.data',delim_whitespace=True,names=columns)
#delim_whitespace指定是否将空格作为sep


# In[3]:


cars.head()


# In[4]:


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

# In[5]:


from sklearn.linear_model import LinearRegression
lr=LinearRegression(fit_intercept=True)
lr.fit(cars[['weight']],cars['mpg'])
predictions=lr.predict(cars[['weight']])
print(predictions[0:5])
print(cars['mpg'][0:5])

plt.scatter(cars['weight'],cars['mpg'],c='r')
plt.scatter(cars['weight'],predictions,c='y')


# In[6]:


#算出均方误差
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(cars['mpg'],predictions)
print(mse)
#根号均方误差
rmse=mse**0.5
print(rmse)


# In[7]:


dummy_cylinders=pd.get_dummies(cars['cylinders'],prefix='cyl')
print(dummy_cylinders.head())


# In[8]:


cars_con=pd.concat([cars,dummy_cylinders],axis=1)
print(cars_con.head())


# In[9]:


dummy_years=pd.get_dummies(cars['model_year'],prefix='year')
print(dummy_years.head())


# In[10]:


cars_concat=pd.concat([cars_con,dummy_years],axis=1)
cars_concat=cars_concat.drop('model_year',axis=1)
cars_concat=cars_concat.drop('cylinders',axis=1)
print(cars_concat.head())


# 使用汽车产地数据统计三分类问题：通过三分2分类完成多分类问题

# In[12]:


shuffled_rows=np.random.permutation(cars_concat.index)
shuffled_cars=cars_concat.iloc[shuffled_rows]
highest_train_row=int(cars_concat.shape[0]*.70)
train=shuffled_cars.iloc[0:highest_train_row]
test=shuffled_cars.iloc[highest_train_row:]

from sklearn.linear_model import LogisticRegression
unique_origins=cars_concat['origin'].unique()
unique_origins.sort()

models={}
features=[c for c in train.columns if c.startswith('cyl') or c.startswith('year')]

for origin in unique_origins:
    model=LogisticRegression()
    
    x_train=train[features]
    y_train=train['origin']==origin
    
    model.fit(x_train,y_train)
    models[origin]=model
    
testing_probs=pd.DataFrame(columns=unique_origins)
print(testing_probs)

for origin in unique_origins:
    x_test=test[features]
    testing_probs[origin]=models[origin].predict_proba(x_test)[:,1]
    
print(testing_probs)


# In[ ]:




