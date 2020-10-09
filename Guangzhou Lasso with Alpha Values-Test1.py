#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
from pandas import DataFrame
import numpy as np
import sklearn
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[20]:


DATAPATH = '/Users/yichu/Work/Year2020/Geography/Student_Research/Sarigai/Manuscript/Environ_Pollu/FinalDataforLassoN_F3.csv'
data = pd.read_csv(DATAPATH)
data.head()


# In[21]:


data.columns


# In[22]:


x = data.drop(['FAC3'], axis=1)
y = data['FAC3']
x.head()
y.head()


# In[23]:


train_x, test_x, train_y, test_y = train_test_split(x,y, test_size=0.15, random_state=1)
train_x.shape
test_x.shape
train_y.shape
test_y.shape


# In[24]:


from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
lm = LinearRegression()
lm_lasso = Lasso(alpha=0.01)
lm
lm_lasso


# In[25]:


lm.fit(train_x, train_y)
lm_lasso.fit(train_x, train_y)


# In[26]:


plt.figure(figsize=(15,10))
ft_importances_lm = pd.Series(lm.coef_, index = x.columns)
ft_importances_lm.plot(kind ='barh')
plt.show()
# print(lm.coef_, x.columns)


# In[13]:


columns=x.columns
dictionary={} 
dictionary["xvars"]=columns
dictionary[ "coeff" ]=list(lm.coef_)
saveName='Regress_Out1.xlsx'
savePath='/Users/yichu/Work/Year2020/Geography/Student_Research/Sarigai/Manuscript/Environ_Pollu/'+saveName
writer=pd.ExcelWriter(savePath)
df=DataFrame(dictionary)
df.to_excel(writer,'Sheet1')
writer.save()


# In[27]:


plt.figure(figsize=(15,10))
ft_importances_lm_lasso = pd.Series(lm_lasso.coef_, index = x.columns)
ft_importances_lm_lasso.plot(kind ='barh')
plt.show()


# In[28]:


columns=x.columns
dictionary={} 
dictionary["xvars"]=columns
dictionary[ "coeff" ]=list(lm_lasso.coef_)
saveName='Lasso_F3_A001_CV15.xlsx'
savePath='/Users/yichu/Work/Year2020/Geography/Student_Research/Sarigai/Manuscript/Environ_Pollu/'+saveName
writer=pd.ExcelWriter(savePath)
df=DataFrame(dictionary)
df.to_excel(writer,'Sheet1')
writer.save()


# In[29]:


print("RSquare Value for Simple Regression TEST data is-")
np.round(lm.score(test_x,test_y)*100,2)
print("RSquare Value for Lasso Regression TEST data is-")
np.round(lm_lasso.score(test_x,test_y)*100,2)


# In[ ]:




