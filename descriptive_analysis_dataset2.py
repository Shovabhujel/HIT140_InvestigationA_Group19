import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df2 = pd.read_csv('dataset2_fully_cleaned.csv')

# Convert the 'time' column to datetime objects
df2['time'] = pd.to_datetime(df2['time'])

# Descriptive Analysis
print("--- Descriptive Statistics for dataset2 ---")
print(df2.describe())
print("\n")

# Visualization 1: Histogram for bat_landing_number
plt.figure(figsize=(10, 6))
sns.histplot(df2['bat_landing_number'], bins=30, kde=True)
plt.title('Distribution of Bat Landing Number')
plt.xlabel('Bat Landing Number')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('bat_landing_number_histogram.png')
plt.close()

# Visualization 2: Scatter plot of food_availability vs. bat_landing_number
plt.figure(figsize=(10, 6))
sns.scatterplot(x='food_availability', y='bat_landing_number', data=df2)
plt.title('Bat Landing Number vs. Food Availability')
plt.xlabel('Food Availability')
plt.ylabel('Bat Landing Number')
plt.tight_layout()
plt.savefig('food_availability_scatter.png')
plt.close()

# Visualization 3: Time-series plot of bat_landing_number
df2_time_series = df2.set_index('time')
plt.figure(figsize=(12, 6))
df2_time_series['bat_landing_number'].plot()
plt.title('Bat Landing Number Over Time')
plt.xlabel('Date and Time')
plt.ylabel('Bat Landing Number')
plt.tight_layout()
plt.savefig('bat_landing_time_series.png')
plt.close()