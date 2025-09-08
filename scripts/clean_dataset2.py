import pandas as pd

print("Starting cleaning process for 'dataset2.csv'...")

# Load the original dataset from the current directory
# Assuming 'dataset2.csv' is in the same folder as this script
df2 = pd.read_csv('../data/dataset2.csv')

# --- Cleaning Step ---

# The only necessary step for this dataset is to convert the 'time' column
# to a standardized datetime format for proper analysis.
df2['time'] = pd.to_datetime(df2['time'], format='%d/%m/%Y %H:%M')

# Save the newly cleaned data to a final CSV file.
df2.to_csv('dataset2_fully_cleaned.csv', index=False)

print("\nCleaning of dataset2 complete.")
print("-> Final file 'dataset2_fully_cleaned.csv' has been created.")
print(f"   Total rows: {len(df2)}")
print("\nFinal data types after cleaning:")
df2.info()

