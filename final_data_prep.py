import pandas as pd

# Load the partially cleaned datasets
print("Loading and preparing 'dataset1_fully_cleaned.csv'...")
df1 = pd.read_csv('dataset1_fully_cleaned.csv')

print("Loading and preparing 'dataset2_fully_cleaned.csv'...")
df2 = pd.read_csv('dataset2_fully_cleaned.csv')

# --- Final Data Type Conversion ---

# Convert date/time columns in dataset1 to a datetime format
date_cols_df1 = ['start_time', 'rat_period_start', 'rat_period_end', 'sunset_time']
for col in date_cols_df1:
    df1[col] = pd.to_datetime(df1[col])

# Convert the 'time' column in dataset2 to a datetime format
df2['time'] = pd.to_datetime(df2['time'])

# --- Validation ---

# Print the info for the first dataset to confirm the data types are correct
print("\n--- Final Check for dataset1 ---")
df1.info()

# Print the info for the second dataset to confirm the data types are correct
print("\n--- Final Check for dataset2 ---")
df2.info()

print("\nAll datasets are now fully cleaned and ready for analysis!")
