import pandas as pd
import statsmodels.api as sm

# Load the cleaned dataset
df2 = pd.read_csv('dataset2_fully_cleaned.csv')

# Define the dependent (Y) and independent (X) variables
y = df2['bat_landing_number']
X = df2[['food_availability', 'rat_minutes']]

# Add a constant to the independent variables for the intercept
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Define the file path in the current directory
file_path = 'final_inferential_results.txt'

# Append regression summary to the same file
with open(file_path, 'a') as f:
    f.write("--- Multiple Linear Regression for dataset2 ---\n")
    f.write(model.summary().as_text())
    f.write("\n\nAll results saved to final_inferential_results.txt\n")

print(f"Regression results appended to {file_path}")