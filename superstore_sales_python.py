import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the dataset
df = pd.read_csv(r'C:\Users\User\Desktop\Github projects\superstore\Sample - Superstore.csv', encoding='ISO-8859-1')
    
print(df.head())

# Check for missing values
print("Missing Data:\n", df.isnull().sum())

# Check the summary statistics
print("\nSummary Statistics:\n", df.describe()
print("\nSummary Info:\n", df.info()


# Convert Order Date and Ship Date to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date']=pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')

# Total Sales by Region

colors= ['orange', 'green', 'blue', 'red']
df.groupby('Region')['Sales'] \
  .sum() \
  .plot.bar(color=colors)

plt.xticks(rotation=0)
plt.title("Top 20 Sales by Region")
plt.xlabel("Total Sales")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# Top 20 states by Sales

df.groupby('State')['Sales'] \
  .sum() \
  .sort_values(ascending=True) \
  .tail(20) \
  .plot.barh(color='blue')

plt.title("Top 20 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.show()

#Top 5 Products by Sales

top5 = df.groupby('Product Name')['Sales'] \
  .sum() \
  .sort_values(ascending=False) \
  .head(5) 

plt.figure(figsize=(10, 6))
plt.pie(top5, 
        labels=top5.index, 
        autopct='%1.1f%%',         
        startangle=140,            
        textprops={'fontsize': 10} 
)
plt.title("Top 5 Products by Sales")
plt.tight_layout()
plt.show()

#Top 10 customers by Sales

df.groupby('Customer Name')['Sales'] \
    .sum() \
    .sort_values(ascending=True) \
    .tail(10) \
    .plot.barh(color='skyblue')

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Names")
plt.tight_layout()
plt.show()

#Total Profit by Product Category

colors= ['purple', 'green', 'blue',]

df.groupby('Category')['Profit'] \
    .sum() \
    .sort_values(ascending=False) \
    .plot.bar(color = colors)

plt.xticks(rotation=0)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()

#Monthly Sales Trend

# Create a proper datetime column for grouping
df['Month_Year'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()

# Group by that month-year and sum
monthly_sales = df.groupby('Month_Year')['Sales'].sum().reset_index()

# Format the month for labeling
monthly_sales['MonthFormatted'] = monthly_sales['Month_Year'].dt.strftime('%b %Y')

#Plot 
plt.figure(figsize=(15, 6))
plt.plot(monthly_sales['MonthFormatted'], monthly_sales['Sales'], marker='o')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

#Sales and Profit scattering by Category

sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category')
plt.xlim(0, 14000)
plt.ylim(-1000, 5000)
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

