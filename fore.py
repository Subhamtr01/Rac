#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# In[46]:


st.set_page_config(page_title="Dashboard",
                  page_icon="bar_chart:",
                  layout="wide")


# In[47]:


data=pd.read_csv('RAC_Datset.csv')
data.shape


# In[48]:


import random
random.seed(35019)
df = data.sample(n=1000, random_state=35019)
df.head()


# In[49]:


df.shape


# In[50]:


df.isnull().sum()


# In[51]:


st.sidebar.header('Please Filter Here:')

Customer_Status = st.sidebar.multiselect(
    "Select the Customer Status:",
    options=df["Customer_Status"].unique(),
    default=df["Customer_Status"].unique())

Gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique())

Marital_Status = st.sidebar.multiselect(
    "Select the Marital Status:",
    options=df["Marital_Status"].unique(),
    default=df["Marital_Status"].unique())

Card_Category = st.sidebar.multiselect(
    "Select the Card Category:",
    options=df["Card_Category"].unique(),
    default=df["Card_Category"].unique())

Education_Level = st.sidebar.multiselect(
    "Select the Education Level:",
    options=df["Education_Level"].unique(),
    default=df["Education_Level"].unique())

df_selection = df.query(
    "Customer_Status ==@Customer_Status & Gender ==@Gender & Marital_Status ==@Marital_Status & Card_Category ==@Card_Category  & Education_Level ==@Education_Level")
st.dataframe(df_selection)


# In[52]:


st.title('Dashboard')
st.markdown('##')
Total_Yearly_Transaction_Amount= int(df_selection['Yearly_Transaction_Amount'].sum())
Total_Credit_Limit= int(df_selection['Credit_Limit'].sum())


# In[53]:


left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader('Total Credit Limit')
    st.subheader(f' {Total_Credit_Limit:,}')

with right_column:
    st.subheader('Total Yearly Transaction Amount')
    st.subheader(f' {Total_Yearly_Transaction_Amount:,}')
st.markdown("---")


# In[54]:





# In[55]:


Pie_chart1= px.pie(df_selection, title='Card used on months', values='Months_on_Use', names='Card_Category',color_discrete_sequence=["mediumpurple"])
Pie_chart2= px.pie(df_selection, title='Card Credit Limit', values='Credit_Limit', names='Card_Category',color_discrete_sequence=["mediumpurple"])
left_column, right_column = st.columns(2)
left_column.plotly_chart(Pie_chart1, use_container_width=True)
right_column.plotly_chart(Pie_chart2, use_container_width=True)


# In[56]:


bar_chart1=px.bar(df_selection, x="Customer_Status", y="Total_Transactions", color="Card_Category", title="Total transaction by customer with different cards",color_discrete_sequence=["mediumpurple"])
bar_chart2=px.bar(df_selection, x="Income_Category", y="Total_Transactions", color="Card_Category", title="Total transaction by Income category with different cards",color_discrete_sequence=["mediumpurple"])
left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart1, use_container_width=True)
right_column.plotly_chart(bar_chart2, use_container_width=True)


# In[57]:


v3 = df_selection.groupby(by=['Marital_Status']).sum()[['Total_Transactions']].sort_values(by=['Total_Transactions'])
fig3 = px.bar(
    v3,
    x='Total_Transactions', y = v3.index,
    orientation='h', title="<b> Total Transactions by Marital Status </b>",
    color_discrete_sequence=["mediumpurple"]* len(v3),
    template="plotly_white",)

v4 = df_selection.groupby(by=['Education_Level']).sum()[['Total_Transactions']].sort_values(by=['Total_Transactions'])
fig4 = px.bar(
    v4,
    x='Total_Transactions', y = v4.index,
    orientation='h', title="<b> Total Transactions by Education Level </b>",
    color_discrete_sequence=["mediumpurple"]* len(v4),
    template="plotly_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig3, use_container_width=True)
right_column.plotly_chart(fig4, use_container_width=True)


# In[58]:


bar_chart3=px.bar(df_selection, x="Education_Level", y="Yearly_Average_Balance", color="Card_Category", title="Yearly Average Balance with Card & Education category",color_discrete_sequence=["mediumpurple"])
bar_chart4=px.bar(df_selection, x="Income_Category", y="Yearly_Transaction_Amount", color="Marital_Status", title="Yearly Transaction Amount with Income & Marital category",color_discrete_sequence=["mediumpurple"])
left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart3, use_container_width=True)
right_column.plotly_chart(bar_chart4, use_container_width=True)


# In[62]:


df2=df_selection.copy()

df2['Customer_Status']=pd.factorize(df2.Customer_Status)[0]
df2['Age']=pd.factorize(df2.Income_Category)[0]
df2['Marital_Status']=pd.factorize(df2.Card_Category)[0]
df2['Card_Category']=pd.factorize(df2.Age)[0]
df2['Yearly_Average_Balance']=pd.factorize(df2.Marital_Status)[0]

df2.rename(columns = {'Customer_Status':'status'}, inplace = True)
df2['Method']=pd.factorize(df2.Credit_Limit)[0]
df2 = df2.drop('Customer_Number',axis=1)
df2 = df2.drop('Total_Transactions',axis=1)
df2.head()

corr=df2.corr()
print(corr)


fig = px.imshow(df2.corr())



hide_st_style = """
            <style>
            #mainMenu {Visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


# In[ ]:




