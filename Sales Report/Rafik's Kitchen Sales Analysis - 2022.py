#!/usr/bin/env python
# coding: utf-8

# # Rafik's Kitchen - Madurai.
# ## Sales Analysis - 2022

# ***
# _**Importing the required libraries & packages**_
# 

# In[1]:


import numpy as np
import pandas as pd
import os
import locale
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import ydata_profiling as pf
from pandas.api.types import CategoricalDtype
import warnings
warnings.filterwarnings('ignore')


# _**Changing The Default Working Directory Path**_

# In[2]:


os.chdir("C:\\Users\\Shridhar\\Desktop\\Viz Projects\\Rafik's Kitchen Sales")


# _**Reading all the necessary datasets using Pandas command**_

# In[3]:


a = pd.read_excel('Jan to Apr 2022.xlsx')
b = pd.read_excel('May to Aug 2022.xlsx')
c = pd.read_excel('Sep to Dec 2022.xlsx')


# _**Getting the number of records(sales) for every four months of 2022 in each datasets**_

# In[4]:


print('Total No. of Sales in Jan. to Apr. 2022 - ',a.shape[0],'\n')
print('Total No. of Sales in May to Aug. 2022 - ',b.shape[0],'\n')
print('Total No. of Sales in  to Sept. to Dec. 2022 - ',c.shape[0],'\n')


# _**Concatting the three datasets using Pandas command to get the data for the whole year of 2022 in a single dataframe and displaying the first three records for verification.**_

# In[5]:


df = pd.concat([a,b,c],axis = 0)
df.head(3)


# _**Getting the Total No. of Sales in the year 2022**_

# In[6]:


print('Total No. of Sales in 2022 -',df.shape[0])


# _**Getting the data types for all the columns in the dataframe.**_

# In[7]:


df.dtypes


# _**Checking for the null values in the dataset**_

# In[8]:


df.isna().sum()


# _**Checking the non-null value counts and dtypes using info command.**_

# In[9]:


df.info()


# _**Getting the description of the data in all numeric columns using describe command**_

# In[10]:


df.describe().T


# _**Getting the correlation values from all numerical columns from the dataframe.**_

# In[11]:


df.corr()


# _**Getting the value counts for all the unique records in the `CATEGORY` column of the dataframe.**_

# In[12]:


df['CATEGORY'].value_counts()


# _**Getting all the unique values of the `CATEGORY` column in the dataframe.**_

# In[13]:


df.CATEGORY.unique()


# _**Replacing the inappropriate data with the right data in the `CATEGORY` column and getting the value counts of the column to check the data in the dataframe.**_

# In[14]:


df['CATEGORY'] = df['CATEGORY'].replace({'Drinks':'Soft Drinks'})
df['CATEGORY'].value_counts()


# _**Similarly getting the value counts for all the unique records in the `PAYMENT MODE` column of the dataframe.**_

# In[15]:


df['PAYMENT MODE'].value_counts()


# _**Getting all the unique values of the `PAYMENT MODE` column in the dataframe.**_

# In[16]:


df['PAYMENT MODE'].unique()


# _**Replacing the inappropriate data with the right data in the `PAYMENT MODE` column and getting the value counts of the column to check the data in the dataframe.**_

# In[17]:


df['PAYMENT MODE'] = df['PAYMENT MODE'].replace({'card':'Card','Card ':'Card'})
df['PAYMENT MODE'].value_counts()


# _**Similarly getting the value counts for all the unique records in the `ITEM` column of the dataframe.**_

# In[18]:


df['ITEM'].value_counts()


# _**Getting all the unique values of the `ITEM` column in the dataframe.**_

# In[19]:


df['ITEM'].unique()


# _**Replacing the inappropriate data with the right data in the `ITEM` column and getting the value counts of the column to check the data in the dataframe.**_

# In[20]:


df['ITEM'] = df['ITEM'].replace({'Chicken Shawarma Roll ':'Chicken Shawarma Roll',
                                 ' Chicken Shawarma  Roll':'Chicken Shawarma Roll',
                                'Chilli Parotta Plain':'Chilli Parotta - Plain','Coco - cola':'Coco Cola',
                                'Grilled Chicken - Full(Garlic)':'Grilled Chicken - Full (Garlic)',
                                'Grilled Chicken Full (Garlic) ':'Grilled Chicken - Full (Garlic)',
                                'Grilled Chicken - Full(Mint)':'Grilled Chicken - Full (Mint)',
                                'Grilled Chicken Full (Mint) ':'Grilled Chicken - Full (Mint)',
                                'Grilled Chicken - Full(Pepper)':'Grilled Chicken - Full (Pepper)',
                                'Grilled Chicken Full (Pepper) ':'Grilled Chicken - Full (Pepper)',
                                'Grilled Chicken - Half(Garlic)':'Grilled Chicken - Half (Garlic)',
                                'Grilled Chicken Half (Garlic) ':'Grilled Chicken - Half (Garlic)',
                                'Grilled Chicken - Half(pepper)':'Grilled Chicken - Half (Pepper)',
                                'Grilled Chicken Half (Pepper) ':'Grilled Chicken - Half (Pepper)',
                                'Grilled Chicken - Quarter(Garlic)':'Grilled Chicken - Quarter (Garlic)',
                                'Grilled Chicken - Quater(Mint)':'Grilled Chicken - Quarter (Mint)',
                                'Grilled Chicken Quarter (Mint) ':'Grilled Chicken - Quarter (Mint)',
                                'Grilled Chicken - Quater(Pepper)':'Grilled Chicken - Quarter (Pepper)',
                                'Grilled Chicken Quarter (Pepper) ':'Grilled Chicken - Quarter (Pepper)',
                                'Lemonade(Sour)':'Lemonade (Sour)','Mojito(Blue)':'Mojito (Blue)',
                                'Mojito(Green)':'Mojito (Green)','Mushroom Plain':'Mushroom - Plain'})
df['ITEM'].value_counts()


# _**Exporting the dataframe as a CSV(Comma Seperated Value) file to the working directory.**_

# In[21]:


df.to_csv('FastFood Sales Data 2022.csv',index = False)


# _**Automated Exploratory Data Analysis (EDA) with ydata_profiling(pandas_profiling)**_

# In[22]:


EDA_Report = pf.ProfileReport(df)
display(EDA_Report)


# _**Exporting the EDA Report as a HTML(Hyper Text Markup Language) file to the working directory.**_

# In[23]:


EDA_Report.to_file('EDA Report.html')


# _**Getting the Correlation Values from all the numeric columns from the dataset using Seaborn Heatmap**_

# In[24]:


plt.rcParams['figure.figsize']=6,4
sns.heatmap(df.corr(),cmap = 'viridis_r', annot = True, square = True)
plt.title('Correlation Heat Map')
plt.show()


# _**Getting the insights for `PAYMENT MODE` to get the number of transactions in the digital transactions & traditional transactions**_

# In[25]:


payment = df['PAYMENT MODE'].value_counts()
print('Total No. of Transactions',payment.values[0]+payment.values[1]+payment.values[2],'\n')
print('The most commonly used payment mode is',payment.index[0],'with',payment.values[0],'transactions. \n')
print('The least used payment mode is',payment.index[2],'with',payment.values[2],'transactions. \n')
print('India is moving towards the Digital Transactions such as UPI and Card. \n')
print('Total no. of digital transactions i.e., Card & UPI are',payment.values[0]+payment.values[1])


# _**Displaying the insights of `PAYMENT MODE` using Pie Chart**_

# In[26]:


plt.rcParams['figure.figsize']=7,5
plt.pie(payment.values,labels=payment.index,startangle=90, colors=('violet','c','y'),
       explode = (0.1,0,0), autopct = '%1.2f%%')
plt.title('Graphical Representation of Payment Mode for all Transactions')
plt.show()


# _**Getting the minimum no. of quantities, maximum no. of quantities and total no. of quantities along with minimum revenue, maximum revenue and total revenue generated for each and every items in the menu list**_

# In[27]:


min_max_sum_orders_revenue = df.groupby('ITEM').agg({'QUANTITY':[np.min,np.max,np.sum],'TOTAL':[np.min,np.max,np.sum]})
min_max_sum_orders_revenue


# _**Getting the insights of the item that is mostly ordered & least ordered by Customers and the no. of units ordered by the Customers**_

# In[28]:


Item = df.groupby('ITEM')['QUANTITY'].sum().sort_values(ascending = False)
print('The best-selling item in the  FastFood Restaurant is',Item.index[0],'with',Item.values[0],'quantities. \n')
print('The least-selling item in the FastFood Restaurant is',Item.index[-1],'with',Item.values[-1],'quantities.')


# _**Displaying the best selling 5 items in the menu along with the no. of quantities ordered using bar chart**_

# In[29]:


plt.rcParams['figure.figsize']=14,6
top_item = sns.barplot(x=Item.index[:5],y=Item.values[:5],palette = 'Greens_r')
for p in top_item.patches:
    top_item.annotate(p.get_height(),(p.get_x() + p.get_width() / 2.0,p.get_height()),
                 ha = 'center',va = 'center',xytext = (0,5),textcoords = 'offset points')
plt.title('Best Selling 5 Items')
plt.xlabel('Items')
plt.ylabel('No. of items sold')
plt.show()


# _**Displaying the least selling 5 items in the menu along with the no. of quantities ordered using bar chart**_

# In[30]:


plt.rcParams['figure.figsize']=15,6
bottom_item = sns.barplot(x=Item.index[-5:],y=Item.values[-5:],palette = 'Reds')
for p in bottom_item.patches:
    bottom_item.annotate(p.get_height(),(p.get_x() + p.get_width() / 2.0,p.get_height()),
                 ha = 'center',va = 'center',xytext = (0,5),textcoords = 'offset points')
plt.title('Least Selling 5 Items')
plt.xlabel('Items')
plt.ylabel('No. of items sold')
plt.show()


# _**Displaying the each and every item in the menu list and the order quantities of them using bar chart**_

# In[31]:


plt.rcParams['figure.figsize']=15,7
sns.barplot(x=Item.index,y=Item.values)
plt.xticks(rotation=90)
plt.title('Total No. of Sales by Items')
plt.xlabel('Items')
plt.ylabel('Total No. of Sales')
plt.show()


# _**Getting the insights of the item in the menu list that generates highest revenue and lowest revenue along with the sum of revenue generated**_

# In[32]:


locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
Revenue = df.groupby('ITEM')['TOTAL'].sum().sort_values(ascending = False)
high_revenue = locale.currency(Revenue.values[0], grouping=True)
low_revenue = locale.currency(Revenue.values[-1], grouping=True)
print('The highest revenue generating item in the  FastFood Restaurant is',Revenue.index[0],'with the sum of',high_revenue,' \n')
print('The lowest revenue generating item in the FastFood Restaurant is',Revenue.index[-1],'with the sum of',low_revenue)


# _**Displaying the high revenue generating 5 items in the menu along with the sum of generated revenue using bar chart**_

# In[33]:


plt.rcParams['figure.figsize']=14,6
high_revenue_item = sns.barplot(x=Revenue.index[:5],y=Revenue.values[:5],palette = 'Blues_r')
for p in high_revenue_item.patches:
    high_revenue_item.annotate(p.get_height(),(p.get_x() + p.get_width() / 2.0,p.get_height()),
                 ha = 'center',va = 'center',xytext = (0,5),textcoords = 'offset points')
plt.title('High Revenue Generating 5 Items')
plt.xlabel('Items')
plt.ylabel('Revenue (₹)')
plt.show()


# _**Displaying the low revenue generating 5 items in the menu along with the sum of generated revenue using bar chart**_

# In[34]:


plt.rcParams['figure.figsize']=15,6
low_revenue_item = sns.barplot(x=Revenue.index[-5:],y=Revenue.values[-5:],palette = 'Oranges')
for p in low_revenue_item.patches:
    low_revenue_item.annotate(p.get_height(),(p.get_x() + p.get_width() / 2.0,p.get_height()),
                 ha = 'center',va = 'center',xytext = (0,5),textcoords = 'offset points')
plt.title('Low Revenue Generating 5 Items')
plt.xlabel('Items')
plt.ylabel('Revenue (₹)')
plt.show()


# _**Displaying the each and every item in the menu list with the revenue generated by them using bar chart**_

# In[35]:


plt.rcParams['figure.figsize']=15,7
sns.barplot(x=Revenue.index,y=Revenue.values,palette = 'autumn_r')
plt.xticks(rotation=90)
plt.title('Total Sales Revenue by Items')
plt.xlabel('Items')
plt.ylabel('Revenue (₹)')
plt.show()


# _**Adding a new column of `DAY OF SALES` to the dataframe by seperating the day name from `DATE` column for further analysis purposes**_

# In[36]:


df['DAY OF SALES']=df['DATE'].dt.day_name()


# _**Arranging the `DAY OF SALES` column in the Calendar Weekly Order for getting the insights as in Calendar order**_

# In[37]:


week_order = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
df['DAY OF SALES'] = df['DAY OF SALES'].astype(CategoricalDtype(categories=week_order, ordered=True))


# _**Getting the insights of the revenue generated for all week days in the year 2022**_

# In[38]:


Day_Sales = df.groupby('DAY OF SALES')['TOTAL'].sum()
print('The Sales Revenue for Every Weekday in 2022')
print(Day_Sales)


# _**Getting the insights of all weekdays that generated high revenue and low revenue with the sum of revenue generated along with the observation**_

# In[39]:


Day_Revenue = df.groupby('DAY OF SALES')['TOTAL'].sum().sort_values(ascending = False)
high_day_revenue = locale.currency(Day_Revenue.values[0], grouping=True)
low_day_revenue = locale.currency(Day_Revenue.values[-1], grouping=True)
weekend_revenue = locale.currency(Day_Revenue.values[0]+Day_Revenue.values[1], grouping=True)
print('The highest revenue generating day is',Day_Revenue.index[0],'& the revenue is',high_day_revenue,'\n')
print('The lowest revenue generating day is',Day_Revenue.index[-1],'& the revenue is',low_day_revenue,'\n')
print('We can clearly observe that weekends are the days where the sales and revenue is high compared to weekdays.\n')
print('The sum of revenue generated on weekends that is on',Day_Revenue.index[1],'and',Day_Revenue.index[0],'are',weekend_revenue)


# _**Displaying the Sum of Revenue Generated for all weekdays using the bar chart with the sum of revenue**_

# In[40]:


plt.rcParams['figure.figsize']=15,6
day_s = sns.barplot(Day_Sales.index,Day_Sales.values,palette='cividis_r')
for p in day_s.patches:
    day_s.annotate(p.get_height(),(p.get_x() + p.get_width() / 2.0,p.get_height()),
                 ha = 'center',va = 'center',xytext = (0,5),textcoords = 'offset points')
plt.title('Revenue Generated for Weekdays - 2022')
plt.xlabel('Day of Sales')
plt.ylabel('Revenue(₹)')
plt.show()


# _**Adding a new column of `MONTH OF SALES` to the dataframe by seperating the month from `DATE` column for further analysis purposes**_

# In[41]:


df['MONTH OF SALES'] = df['DATE'].dt.month_name()


# _**Arranging the `MONTH OF SALES` column in the Calendar Monthly Order for getting the insights as in Calendar order**_

# In[42]:


month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
df['MONTH OF SALES'] = df['MONTH OF SALES'].astype(CategoricalDtype(categories=month_order, ordered=True))


# _**Getting the insights of the revenue generated for each and every month in the year 2022**_

# In[43]:


Monthly_Sales = df.groupby('MONTH OF SALES')['TOTAL'].sum()
print('The Sales Revenue for Every Month in 2022')
print(Monthly_Sales)


# _**Getting the insights of the month which generated high revenue and low revenue with the sum of revenue generated**_

# In[44]:


Monthly_Revenue = df.groupby('MONTH OF SALES')['TOTAL'].sum().sort_values(ascending = False)
high_monthly_revenue = locale.currency(Monthly_Revenue.values[0], grouping=True)
low_monthly_revenue = locale.currency(Monthly_Revenue.values[-1], grouping=True)
print('The month that generated high revenue is',Monthly_Revenue.index[0],'& the generated revenue is',high_monthly_revenue)
print('\nThe month that generated low revenue is',Monthly_Revenue.index[-1],'& the generated revenue is',low_monthly_revenue)


# _**Plotting the line graph to show the data trend of generated revenue for every month with the value of revenue generated**_

# In[45]:


plt.rcParams['figure.figsize']=15,8
plt.plot(Monthly_Sales.index,Monthly_Sales.values)
for i, txt in enumerate(Monthly_Sales.values):
    plt.annotate(txt,(Monthly_Sales.index[i],Monthly_Sales.values[i]),textcoords = 'offset points',
                xytext = (0,10),ha = 'center')
    plt.scatter(Monthly_Sales.index[i],Monthly_Sales.values[i],color = 'red',s = 40,zorder = 5)
plt.title('Monthly Sales Trend - 2022')    
plt.xlabel('Month of Sales')    
plt.ylabel('Revenue (₹)')
plt.show()

