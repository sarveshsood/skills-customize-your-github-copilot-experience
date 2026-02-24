# Python Statistics Assignment
# Starter code for data analysis and statistical calculations with pandas and numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import scipy.stats as stats  # For advanced statistical tests

# Set up plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette('husl')

# TODO: Task 1 - Data Loading and Basic Statistics
def data_loading_basics():
    # Create sample data
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [25, 30, 35, 28, 32],
        'salary': [50000, 60000, 70000, 55000, 65000],
        'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
    }

    df = pd.DataFrame(data)
    print("Sample DataFrame:")
    print(df)
    print("\nBasic Statistics:")
    print(df.describe())

    # Numpy array operations
    ages = np.array(df['age'])
    salaries = np.array(df['salary'])

    print(f"\nMean age: {np.mean(ages):.2f}")
    print(f"Median salary: ${np.median(salaries):.2f}")
    print(f"Standard deviation of salaries: ${np.std(salaries):.2f}")
    print(f"Variance of ages: {np.var(ages):.2f}")

    return df

# TODO: Task 2 - Data Manipulation and Cleaning
def data_manipulation_cleaning(df):
    # Add some missing data for demonstration
    df_clean = df.copy()
    df_clean.loc[2, 'salary'] = np.nan
    df_clean.loc[4, 'age'] = np.nan

    print("DataFrame with missing values:")
    print(df_clean)
    print(f"\nMissing values count:\n{df_clean.isnull().sum()}")

    # Handle missing values
    df_clean['salary'] = df_clean['salary'].fillna(df_clean['salary'].mean())
    df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())

    print("\nDataFrame after filling missing values:")
    print(df_clean)

    # Remove duplicates (add a duplicate first)
    df_clean = pd.concat([df_clean, df_clean.iloc[0:1]], ignore_index=True)
    print(f"\nDataFrame with duplicate:\n{df_clean}")
    print(f"Shape before removing duplicates: {df_clean.shape}")

    df_clean = df_clean.drop_duplicates()
    print(f"Shape after removing duplicates: {df_clean.shape}")

    # Group by department
    dept_stats = df_clean.groupby('department').agg({
        'salary': ['mean', 'count'],
        'age': 'mean'
    })
    print(f"\nDepartment statistics:\n{dept_stats}")

    return df_clean

# TODO: Task 3 - Statistical Analysis
def statistical_analysis(df):
    # Correlation analysis
    numeric_cols = ['age', 'salary']
    correlation_matrix = df[numeric_cols].corr()
    print("Correlation Matrix:")
    print(correlation_matrix)

    # Create contingency table
    contingency = pd.crosstab(df['department'], pd.cut(df['age'], bins=3, labels=['Young', 'Middle', 'Senior']))
    print(f"\nContingency Table (Department vs Age Group):\n{contingency}")

    # Simple linear regression simulation
    x = df['age']
    y = df['salary']

    # Calculate slope and intercept
    slope = np.cov(x, y)[0, 1] / np.var(x)
    intercept = np.mean(y) - slope * np.mean(x)

    print(".2f")
    print(".2f")

    # Predict salaries
    df['predicted_salary'] = intercept + slope * df['age']
    print(f"\nActual vs Predicted Salaries:\n{df[['name', 'salary', 'predicted_salary']]}")

    return correlation_matrix

# TODO: Task 4 - Data Visualization for Statistics
def statistical_visualization(df, correlation_matrix):
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Statistical Analysis Visualizations', fontsize=16)

    # Histogram of salaries
    axes[0, 0].hist(df['salary'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Salary Distribution')
    axes[0, 0].set_xlabel('Salary ($)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].axvline(df['salary'].mean(), color='red', linestyle='--', label='.0f')
    axes[0, 0].legend()

    # Box plot of ages by department
    sns.boxplot(x='department', y='age', data=df, ax=axes[0, 1])
    axes[0, 1].set_title('Age Distribution by Department')
    axes[0, 1].set_xlabel('Department')
    axes[0, 1].set_ylabel('Age')

    # Scatter plot with regression line
    axes[1, 0].scatter(df['age'], df['salary'], alpha=0.7, color='green')
    axes[1, 0].set_title('Age vs Salary Scatter Plot')
    axes[1, 0].set_xlabel('Age')
    axes[1, 0].set_ylabel('Salary ($)')

    # Add regression line
    x_range = np.linspace(df['age'].min(), df['age'].max(), 100)
    slope = np.cov(df['age'], df['salary'])[0, 1] / np.var(df['age'])
    intercept = np.mean(df['salary']) - slope * np.mean(df['age'])
    y_range = intercept + slope * x_range
    axes[1, 0].plot(x_range, y_range, color='red', label='Regression Line')
    axes[1, 0].legend()

    # Correlation heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=axes[1, 1])
    axes[1, 1].set_title('Correlation Heatmap')

    plt.tight_layout()
    plt.savefig('statistical_analysis_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("=== Data Loading and Basic Statistics ===")
    df = data_loading_basics()

    print("\n=== Data Manipulation and Cleaning ===")
    df_clean = data_manipulation_cleaning(df)

    print("\n=== Statistical Analysis ===")
    corr_matrix = statistical_analysis(df_clean)

    print("\n=== Statistical Visualization ===")
    statistical_visualization(df_clean, corr_matrix)