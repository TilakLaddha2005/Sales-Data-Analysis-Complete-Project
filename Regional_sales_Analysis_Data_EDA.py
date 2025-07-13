import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Monthly Revenue Trend (Combined Across Years)

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

df['month'] = df['order_date'].dt.strftime('%B')

monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()

month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
monthly_revenue['month'] = pd.Categorical(monthly_revenue['month'], categories=month_order, ordered=True)
monthly_revenue = monthly_revenue.sort_values('month')

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_revenue, x='month', y='revenue', marker='o', linewidth=2.5)
plt.title('Monthly Revenue Trend (Combined Across Years)', fontsize=18, weight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Revenue', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insight 1: April is the Peak Revenue Month

# Insight 2: June Experiences the Sharpest Revenue Drop

# Insight 3: Revenue Stabilizes in the Second Half of the Year

## Top 10 Products by Revenue

top_products = df.groupby('product_name')['revenue'].sum().reset_index()
top_products = top_products.sort_values(by='revenue', ascending=False).head(10)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(data=top_products, x='revenue', y='product_name', palette='Blues_d')

plt.title('Top 10 Products by Revenue', fontsize=16, weight='bold')
plt.xlabel('Total Revenue', fontsize=14)
plt.ylabel('Product Name', fontsize=14)
plt.tight_layout()
plt.show()

# Insights:
# Product 26 and Product 25 generate significantly higher revenue compared to all other products, indicating they are the primary revenue drivers.

# The revenue contribution gradually declines after the top 3 products, showing a clear concentration of earnings among a few products.

# Products like Product 1 to Product 4 still maintain strong performance and could be leveraged further through focused promotion or bundling with top performers.

## Revenue Distribution by Sales Channel

import pandas as pd
import matplotlib.pyplot as plt

channel_revenue = df.groupby('channel')['revenue'].sum().reset_index()

plt.figure(figsize=(5, 5))
plt.pie(channel_revenue['revenue'], labels=channel_revenue['channel'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Revenue Distribution by Sales Channel', fontsize=16, weight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Insights:
# Wholesale channel contributes the majority of revenue, accounting for over half of the total share, which indicates it is the dominant sales driver.

# Distributor channel holds a strong secondary position with about one third of the revenue, showing consistent performance across the market.

# Export channel generates the smallest portion of revenue, suggesting potential for expansion or reevaluation of international sales strategy.

## Unit Price Distribution per Product

# plt.figure(figsize=(14, 6))
# sns.boxplot(data=df, x='product_name', y='unit_price')
# plt.xticks(rotation=90)
# plt.title('Unit Price Distribution per Product', fontsize=16, weight='bold')
# plt.xlabel('Product Name')
# plt.ylabel('Unit Price')
# plt.tight_layout()
# plt.show()

# Insights:
# Several products including Product 20 and Product 26 show wide price ranges with many outliers, indicating significant price variation possibly due to customization or dynamic pricing strategies

# Products like Product 6 and Product 29 have relatively lower and more consistent unit prices, suggesting a stable pricing strategy or standardized offering

# A few products such as Product 27 and Product 22 show high median prices and large interquartile ranges, which may reflect premium product positioning or bundled offerings

## Top 10 States by Revenue & Order Count

# top_states = df.groupby('state_name').agg({
#     'revenue': 'sum',
#     'order_number': 'count'
# }).reset_index()

# top_states = top_states.sort_values(by='revenue', ascending=False).head(10)

# plt.figure(figsize=(14, 6))
# sns.barplot(data=top_states, x='state_name', y='revenue', palette='Greens_d')
# plt.title('Top 10 States by Revenue', fontsize=16, weight='bold')
# plt.xlabel('State Name')
# plt.ylabel('Total Revenue')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(14, 6))
# sns.barplot(data=top_states, x='state_name', y='order_number', palette='Purples_d')
# plt.title('Top 10 States by Order Count', fontsize=16, weight='bold')
# plt.xlabel('State Name')
# plt.ylabel('Order Count')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Insights:
# California is the leading state by both revenue and order count, indicating it is the strongest performing market in terms of volume and value

# Some states like Texas and Florida show high revenue but relatively lower order counts, which suggests higher average order value in those states

# States like Michigan and Massachusetts appear at the bottom of both lists, signaling potential regions for targeted sales growth or marketing efforts

## Average Profit Margin by Sales Channel

# df['profit_margin'] = (df['revenue'] - df['total cost']) / df['revenue']

# avg_margin_by_channel = df.groupby('channel')['profit_margin'].mean().reset_index()

# plt.figure(figsize=(8, 5))
# ax = sns.barplot(data=avg_margin_by_channel, x='channel', y='profit_margin', palette='Set2')
# plt.title('Average Profit Margin by Sales Channel', fontsize=16, weight='bold')
# plt.xlabel('Sales Channel')
# plt.ylabel('Average Profit Margin')
# plt.ylim(0, 1)

# for i in ax.containers:
#     ax.bar_label(i, fmt='%.2f', padding=3)

# plt.tight_layout()
# plt.show()

# Insights:
# Distributor and Export channels yield the highest average profit margins, both at approximately 0.38

# Wholesale has a slightly lower average profit margin at 0.37 despite contributing the highest revenue

# The profit margins across all channels are close, indicating consistent cost control and pricing across different sales methods

## Top & Bottom 10 Customers by Revenue

# top_customers = df.groupby('customer_name')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(10)

# bottom_customers = df.groupby('customer_name')['revenue'].sum().reset_index().sort_values('revenue', ascending=True).head(10)

# plt.figure(figsize=(12, 5))
# sns.barplot(data=top_customers, x='revenue', y='customer_name', palette='Blues_r')
# plt.title('Top 10 Customers by Revenue')
# plt.xlabel('Total Revenue')
# plt.ylabel('Customer Name')
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(12, 5))
# sns.barplot(data=bottom_customers, x='revenue', y='customer_name', palette='Reds')
# plt.title('Bottom 10 Customers by Revenue')
# plt.xlabel('Total Revenue')
# plt.ylabel('Customer Name')
# plt.tight_layout()
# plt.show()

## Customer Segmentation: Revenue vs Profit Margin

# df['profit_margin'] = (df['revenue'] - df['total cost']) / df['revenue']

# customer_seg = df.groupby('customer_name').agg({
#     'revenue': 'sum',
#     'profit_margin': 'mean'
# }).reset_index()

# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=customer_seg, x='revenue', y='profit_margin', hue='profit_margin', palette='viridis', size='revenue', sizes=(40, 400), legend=False)

# plt.title('Customer Segmentation: Revenue vs Profit Margin')
# plt.xlabel('Total Revenue')
# plt.ylabel('Average Profit Margin')
# plt.tight_layout()
# plt.show()

# Insights:
# Most customers cluster in the mid-revenue and mid-profit margin zone suggesting a balanced but average contribution to the business

# There are a few high-revenue customers with relatively lower profit margins which may indicate heavy discounts or higher service costs

# High profit margin customers tend to have lower revenue indicating they may be smaller but more efficient clients in terms of profitability

# Correlation Heatmap

# correlation_matrix = df[['order_quantity', 'unit_price', 'revenue', 'total cost']].corr()

# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Heatmap')
# plt.tight_layout()
# plt.show()

# Insights
# revenue and total cost have a very strong positive correlation indicating that as revenue increases the associated costs also rise proportionally

# unit price is strongly correlated with revenue and cost suggesting that pricing significantly influences both total income and expense

# order quantity has a moderate positive correlation with both revenue and total cost which shows that higher sales volume contributes to revenue but not as strongly as unit price

