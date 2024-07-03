import glob
import pandas as pd

# Specify the directory path where your CSV files are located
directory_path = './data/'

# Specify the product type you are interested in
product_type = "pink morsel"

# Use glob to find all CSV files in the directory
file_paths = glob.glob(directory_path + '*.csv')

# Initialize an empty list to store DataFrames
dfs = []

# Iterate over each file path and read the CSV into a DataFrame
for file_path in file_paths:
    df = pd.read_csv(file_path)

    # Filter rows where product type matches "pink morsel"
    df_filtered = df[df['product'] == product_type]

    # Convert price to numeric, removing '$' and converting to float
    df_filtered['price'] = df_filtered['price'].replace('[\$,]', '', regex=True).astype(float)

    # Calculate sales by multiplying quantity and price
    df_filtered['sales'] = df_filtered['quantity'] * df_filtered['price']

    # Select only the relevant columns for final output
    df_final = df_filtered[['sales', 'date', 'region']]

    # Append filtered DataFrame to the list
    dfs.append(df_final)

# Concatenate all filtered DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Format the sales column as currency
combined_df['sales'] = combined_df['sales'].map('${:,.2f}'.format)

# Print the combined DataFrame
print(combined_df)