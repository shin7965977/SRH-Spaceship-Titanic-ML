#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import plotly.express as px


# In[2]:


#Read the csv file and show the data
df = pd.read_csv(r"spaceship_titanic_e.csv")
df.head()


# In[4]:


#Dropping the unnecessary columns
df=df.drop(['PassengerId', 'Cabin','Name','GroupId','PassengerIdInGroup','Surname'], axis=1)


# In[7]:


#Bar plot for transported column
df['Transported'].value_counts().plot(kind='bar')


# In[22]:


#Bar plot of Nan values of all columns
relativenan=df.isna().sum()/df.count()
relativenan[df.isna().sum()>0].plot(kind='bar')


# In[9]:


#Box plot of age column to track outliers
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Box(
    y=df["Age"],
    name="Outliers",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.show()


# In[24]:


#box plot of all numerical columns to track outliers
fig = go.Figure()
fig.add_trace(go.Box(
    y=df["RoomService"],
    name="RoomService",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.add_trace(go.Box(
    y=df["FoodCourt"],
    name="FoodCourt",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.add_trace(go.Box(
    y=df["ShoppingMall"],
    name="ShoppingMall",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.add_trace(go.Box(
    y=df["Spa"],
    name="Spa",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.add_trace(go.Box(
    y=df["VRDeck"],
    name="VRDeck",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.show()


# In[16]:


#box plot of MembersOfGroupById and MembersOfFamilyBySurname columns to track outliers
fig = go.Figure()
fig.add_trace(go.Box(
    y=df["MembersOfGroupById"],
    name="MembersOfGroupById",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.add_trace(go.Box(
    y=df["MembersOfFamilyBySurname"],
    name="MembersOfFamilyBySurname",
    boxpoints='outliers',
    marker_color='rgb(107,174,214)',
    line_color='rgb(107,174,214)'
))
fig.show()


# In[18]:


#Correlation between the numerical columns
df.corr(numeric_only=True)


# In[19]:


#Heatmap to show the correlation
fig = px.imshow(df.corr(numeric_only=True),text_auto=True)
fig.show()


# In[26]:


#Bar plot for HomePlanet column
df['HomePlanet'].value_counts().plot(kind='bar',edgecolor="black")


# In[29]:


#Bar plot for CryoSleep column
df['CryoSleep'].value_counts().plot(kind='bar',edgecolor="black")


# In[31]:


#Bar plot for Destination column
df['Destination'].value_counts().plot(kind='bar',edgecolor="black")


# In[33]:


#Bar plot for VIP column
df['VIP'].value_counts().plot(kind='bar',edgecolor="black")


# In[35]:


#Bar plot for CabinDeck column
df['CabinDeck'].value_counts().plot(kind='bar',edgecolor="black")


# In[37]:


#Bar plot for CabinNum column
df["CabinNum"].value_counts().plot.hist(bins=30, edgecolor="black")


# In[40]:


#Bar plot for CabinSide column
df['CabinSide'].value_counts().plot(kind='bar',edgecolor="black")


# In[46]:


#Bar plot for AgeBinned column
df['AgeBinned'].value_counts().plot(kind='bar',edgecolor="black")


# In[83]:


#Scattermatrix plot of all numerical columns
fig = px.scatter_matrix(df,dimensions=df.select_dtypes(include='number'),color="Transported")
fig.update_traces(diagonal_visible=False)
fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=5,  
        color="Black"
    )
)

fig.show()


# In[86]:


#Pivot table for HomePlanet column compared to Transported(target) column
pivot = df.groupby(["HomePlanet","Transported"])["Transported"].count().unstack()
pivot


# In[87]:


#Bar plot of pivot table
pivot.plot.bar()


# In[88]:


#Pivot table for CryoSleep column compared to Transported(target) column
pivot = df.groupby(["CryoSleep","Transported"])["Transported"].count().unstack()
pivot


# In[89]:


#Bar plot of pivot table
pivot.plot.bar()


# In[90]:


#Pivot table for Destination column compared to Transported(target) column
pivot = df.groupby(["Destination","Transported"])["Transported"].count().unstack()
pivot


# In[91]:


#Bar plot of pivot table
pivot.plot.bar()


# In[92]:


#Pivot table for VIP column compared to Transported(target) column
pivot = df.groupby(["VIP","Transported"])["Transported"].count().unstack()
pivot


# In[93]:


#Bar plot of pivot table
pivot.plot.bar()


# In[94]:


#Pivot table for CabinDeck column compared to Transported(target) column
pivot = df.groupby(["CabinDeck","Transported"])["Transported"].count().unstack()
pivot


# In[95]:


#Bar plot of pivot table
pivot.plot.bar()


# In[96]:


#Pivot table for CabinNum column compared to Transported(target) column
pivot = df.groupby(["CabinNum","Transported"])["Transported"].count().unstack()
pivot


# In[97]:


#Bar plot of pivot table
pivot.plot.bar()


# In[98]:


#Pivot table for CabinSide column compared to Transported(target) column
pivot = df.groupby(["CabinSide","Transported"])["Transported"].count().unstack()
pivot


# In[99]:


#Bar plot of pivot table
pivot.plot.bar()


# In[100]:


#Pivot table for AgeBinned column compared to Transported(target) column
pivot = df.groupby(["AgeBinned","Transported"])["Transported"].count().unstack()
pivot


# In[101]:


#Bar plot of pivot table
pivot.plot.bar()

