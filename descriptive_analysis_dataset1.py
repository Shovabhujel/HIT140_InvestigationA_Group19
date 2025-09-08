import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df1 = pd.read_csv('../data/dataset1_fully_cleaned.csv')

# Convert relevant date columns to datetime objects
df1['start_time'] = pd.to_datetime(df1['start_time'])
df1['rat_period_start'] = pd.to_datetime(df1['rat_period_start'])
df1['rat_period_end'] = pd.to_datetime(df1['rat_period_end'])
df1['sunset_time'] = pd.to_datetime(df1['sunset_time'])

# Descriptive Analysis
print("--- Descriptive Statistics for dataset1 ---")
print(df1.describe())
print("\n")

# Visualization 1: Histogram for hours_after_sunset
plt.figure(figsize=(10, 6))
sns.histplot(df1['hours_after_sunset'], bins=30, kde=True)
plt.title('Distribution of Hours After Sunset')
plt.xlabel('Hours After Sunset')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('hours_after_sunset_histogram.png')
plt.close()

# Visualization 2: Bar chart for risk vs. reward
risk_reward_counts = df1.groupby(['risk', 'reward']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))
risk_reward_counts.plot(kind='bar')
plt.title('Count of Observations by Risk and Reward')
plt.xlabel('Risk (1 = High Risk)')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['Low', 'High'], rotation=0)
plt.legend(title='Reward (1 = High Reward)')
plt.tight_layout()
plt.savefig('risk_reward_bar_chart.png')
plt.close()

# Visualization 3: Box plot for bat_landing_to_food by habit
plt.figure(figsize=(10, 6))
sns.boxplot(x='habit', y='bat_landing_to_food', data=df1)
plt.title('Distribution of Bat Landing to Food by Habit')
plt.xlabel('Habit')
plt.ylabel('Bat Landing to Food (seconds)')
plt.tight_layout()
plt.savefig('bat_landing_by_habit_boxplot.png')
plt.close()
