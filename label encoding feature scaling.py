#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r"C:\Users\Parimal\Desktop\chegg 23122022.csv")
data


# # Label Encoding

# In[3]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['E']=le.fit_transform(data['E'])


# In[4]:


data


# In[5]:


independent_features=data.iloc[:,:-1].values
dependent_feature=data.iloc[:,-1].values
independent_features


# In[6]:


from imblearn.over_sampling import RandomOverSampler
ro=RandomOverSampler()
x_data,y_data=ro.fit_resample(independent_features,dependent_feature)

from collections import Counter
print(Counter(y_data))


# # Feature Scalling


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_data=sc.fit_transform(x_data)


# Train test Spite
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data)



from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='gini')
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
accuracy





