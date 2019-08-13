#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


admissions=pd.read_csv('D:/pydata/admissions.csv')


# In[3]:


admissions.head()


# In[4]:


admissions['actual_label']=admissions['admit']
admissions=admissions.drop('admit',axis=1)


# In[5]:


admissions


# In[6]:


#对数据进行洗牌
shuffled_index=np.random.permutation(admissions.index)
shuffled_admissions=admissions.loc[shuffled_index]
admissions=shuffled_admissions.reset_index()


# In[7]:


#切分为5块
admissions.ix[0:128,'fold']=1
admissions.ix[129:257,'fold']=2
admissions.ix[258:386,'fold']=3
admissions.ix[387:514,'fold']=4
admissions.ix[515:644,'fold']=5

admissions['fold']=admissions['fold'].astype('int')


# In[8]:


admissions.head()


# In[9]:


admissions.tail()


# 对切分的数据进行测试统计

# In[15]:


from sklearn.linear_model import LogisticRegression
fold_ids=[1,2,3,4,5]
def train_and_test(df,folds):
    fold_accuracies=[]
    for fold in folds:
        model=LogisticRegression()
        train=admissions[admissions['fold']!=fold]
        test=admissions[admissions['fold']==fold]
        model.fit(train[['gpa']],train['actual_label'])
        labels=model.predict(test[['gpa']])
        test['predicted_label']=labels
        
        matches=test['predicted_label']==test['actual_label']
        correct_predictions=test[matches]
        fold_accuracies.append(len(correct_predictions)/float(len(test)))
    return(fold_accuracies)

accuracies=train_and_test(admissions,fold_ids)
print(accuracies)
average_accuracy=np.mean(accuracies)
print(average_accuracy)


# 简化操作Kfold方法

# In[16]:


import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

kf=KFold(n_splits=5,shuffle=True,random_state=8)
#创建回归模型
lr=LogisticRegression()
#roc_auc返回交叉验证的得分结果
accuracies=cross_val_score(lr,admissions[['gpa']],admissions['actual_label'],scoring='roc_auc',cv=kf)
average_accuracy=sum(accuracies)/len(accuracies)
print(accuracies)
print(average_accuracy)


# In[ ]:




