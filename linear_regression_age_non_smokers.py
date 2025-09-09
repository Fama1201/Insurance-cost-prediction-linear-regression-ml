import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Optional: style for plots
sns.set_style("darkgrid")

# Load dataset
medical_df = pd.read_csv('medical.csv')

# Filter non-smokers
non_smoker_df = medical_df[medical_df.smoker == 'no']

# Print first rows
#print(non_smoker_df.head())

# Helper function: linear estimation
def estimate_charges(age, w, b):
    return w * age + b 

# RMSE function
def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))

# Function to try parameters
def try_parameters(w, b):
    ages = non_smoker_df['age']
    actual_charges = non_smoker_df['charges']
    
    # Predictions
    estimated_charges = estimate_charges(ages, w, b)
    
    # Calculate loss
    loss = rmse(actual_charges, estimated_charges)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(ages, actual_charges, alpha=0.5, label='Actual Charges')
    plt.plot(ages, estimated_charges, 'r-', label=f'Estimated Charges (RMSE={loss:.2f})')
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.title(f'Estimated vs Actual Charges (w={w}, b={b})')
    plt.legend()
    plt.show()
    
    print(f"RMSE (Loss) = {loss:.2f}")

# Try sample parameters
try_parameters(280, -4000)
