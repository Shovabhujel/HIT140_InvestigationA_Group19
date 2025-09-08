import pandas as pd

print("Starting cleaning process for 'dataset1.csv'...")

# Load the original dataset from the current directory
# Assuming 'dataset1.csv' is in the same folder as this script
df1 = pd.read_csv('dataset1.csv')

# --- Cleaning Steps ---

# 1. Remove rows with anomalous semicolon entries in the 'habit' column.
# The `~` operator is a logical NOT, which keeps rows that DO NOT match the condition.
df1_cleaned = df1[~df1['habit'].str.contains(';', na=False)].copy()

# 2. Fill all remaining missing values (NaN) in the 'habit' column with 'unspecified'.
# This ensures there are no empty entries in this column.
df1_cleaned['habit'] = df1_cleaned['habit'].fillna('unspecified')

# 3. Convert all relevant date/time columns to a standard datetime format.
# This is crucial for any time-series analysis and plotting.
date_columns_df1 = ['start_time', 'rat_period_start', 'rat_period_end', 'sunset_time']
for col in date_columns_df1:
    df1_cleaned[col] = pd.to_datetime(df1_cleaned[col], format='%d/%m/%Y %H:%M')

# Save the newly cleaned data to a final CSV file.
df1_cleaned.to_csv('dataset1_fully_cleaned.csv', index=False)

print("\nCleaning of dataset1 complete.")
print("-> Final file 'dataset1_fully_cleaned.csv' has been created.")
print(f"   Original rows: {len(df1)}")
print(f"   Final rows: {len(df1_cleaned)}")
print("\nFinal data types after cleaning:")
df1_cleaned.info()
