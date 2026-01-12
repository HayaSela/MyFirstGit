import pandas as pd

# Creating a dictionary with sales data
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Price': [1200, 25, 300, 75],
    'Quantity': [5, 50, 10, 20]
}

# Converting data to a Pandas DataFrame
df = pd.DataFrame(data)

# Calculating Total Revenue for each product
df['Revenue'] = df['Price'] * df['Quantity']

print("--- Sales Report ---")
print(df)
print("\nTotal Revenue: $", df['Revenue'].sum())
