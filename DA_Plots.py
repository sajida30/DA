#!/usr/bin/env python
# coding: utf-8

# # Different types of plots 

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("/home/dai/Downloads/pizza.csv")


# In[3]:


df


# # Scatter plot 

# In[4]:


plt.scatter(x=df['Promote'],y=df['Sales'])


# # Bar plot

# In[18]:


sns.barplot(data=df, x="Promote", y="Sales")


# In[5]:


concrete=pd.read_csv("/home/dai/Downloads/Concrete_Data.csv")


# In[6]:


concrete


# # Heatmap

# In[9]:


sns.heatmap(concrete.corr(),
           xticklabels=concrete.corr().columns,
           yticklabels=concrete.corr().columns,annot=True)


# In[10]:


plt.show()


# In[11]:


iris=pd.read_csv("/home/dai/Downloads/iris.csv")


# In[12]:


iris


# # Pair plot

# In[13]:


sns.pairplot(iris)


# # Box plot

# In[15]:


sns.boxplot(x='Species',y='Petal.Length',data=iris)


# # Strip plot

# A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.

# In[17]:


ax=sns.stripplot(x='Species',y='Sepal.Length',data=iris,jitter=True,edgecolor='gray')


# In[19]:


plant=pd.read_csv("/home/dai/Downloads/PlantGrowth.csv")


# In[20]:


plant


# # Cat plot

# In[21]:


sns.catplot(data=plant, x="group", y="weight")


# # Count plot

# Show the number of datapoints with each value of a categorical variable:

# In[22]:


sns.countplot(x=plant["group"])


# # Pie Plot

# In[27]:


rose=pd.read_csv("/home/dai/Downloads/Rose.csv")
rose


# In[30]:


plt.pie(rose["Sales"], labels = rose["Month"])


# # Line Plot

# In[32]:


sns.lineplot(data=rose, x="Month", y="Sales")


# # Bar Graph

# In[33]:


sns.barplot(data=rose, x="Month", y="Sales")


# In[ ]:




