# importing lib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sheets = pd.read_excel('C:/Users/Tilak Laddha/OneDrive/Desktop/New folder (4)/PROJECT TO DO/Sales Analysis end to end project (PSPB) SP/Regional Sales Dataset.xlsx' , sheet_name= None)

# Assign dataframes to each sheet

df_sales = sheets['Sales Orders']
df_customers = sheets['Customers']
df_products = sheets['Products']
df_regions = sheets['Regions']
df_state_reg = sheets['State Regions']
df_budgets = sheets['2017 Budgets']

# Error of header
new_header = df_state_reg.iloc[0]
df_state_reg.columns = new_header
df_state_reg = df_state_reg[1:].reset_index(drop=True)

df_state_reg.head(5)

# checking Nulls

df_sales.isnull().sum()
df_customers.isnull().sum()
df_products.isnull().sum()
df_regions.isnull().sum()
df_state_reg.isnull().sum()
df_budgets.isnull().sum()

# Data Cleaning

# Merging Tables

# Merging sales - customers

df = df_sales.merge(
    df_customers,
    how='left',
    left_on='Customer Name Index',
    right_on='Customer Index'
)

df = df.drop('Customer Index', axis=1)
df.head(5)

# Merging sales - customers - products

df = df.merge(
    df_products,
    how='left',
    left_on='Product Description Index',
    right_on='Index'
)

df= df.drop('Index', axis=1)
df.head(5)

# Merging sales - customers - products - regions

df = df.merge(
    df_regions,
    how='left',
    left_on='Delivery Region Index',
    right_on='id'
)

df.head(5)

# Merging sales - customers - products - regions - state region

df = df.merge(
    df_state_reg[['State Code','Region']],
    how='left',
    left_on='state_code',
    right_on='State Code'
)

df.head(5)

# repeat columns drop

cols_to_drop = ['id','State Code']
df = df.drop(columns=cols_to_drop,errors='ignore')
df.head(5)

# Merging sales - customers - products - regions - state region - 2017 budgets

df = df.merge(
    df_budgets,
    how='left',
    left_on='Product Name',
    right_on='Product Name'
)

# Convert columns name to lower

df.columns = df.columns.str.lower()

df.columns.values

cols_to_keep =[
    'ordernumber',
    'orderdate',
    'customer names',
    'channel',
    'product name',
    'order quantity',
    'unit price',
    'line total',
    'total unit cost',
    'state_code',
    'county',
    'state',
    'region',
    'latitude',
    'longitude',
    '2017 budgets'
]

df = df[cols_to_keep]

# Rename the colums

df = df.rename(columns={
    'ordernumber':'order_number',
    'orderdate':'order_date',
    'customer names':'customer_name',
    'product name':'product_name',
    'order quantity':'order_quantity',
    'unit price':'unit_price',
    'line total':'revenue',
    'total unit cost':'cost',
    'state_code':'state',
    'state':'state_name',
    'latitude':'lat',
    'longitude':'lon',
    '2017 budgets':'budget'
})

#convert order_date to datetime values
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# blank out bugets for non-2017 orders
df.loc[df['order_date'].dt.year != 2017,'budget'] = pd.NA

df[['order_date','product_name','revenue','budget']].head(5)

df.to_csv('final.csv', index=False)

df_2017 = df[df['order_date'].dt.year == 2017]
df_2017.head(5)

df_2017.to_csv('2017_data.csv',index=False)