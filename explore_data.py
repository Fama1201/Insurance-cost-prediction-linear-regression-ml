import pandas as pd
import plotly.express as px
import plotly.io as pio

# -----------------------------
# Configure Plotly to open figures in the web browser
# This avoids freezing issues in terminal environments
# -----------------------------
pio.renderers.default = "browser"

# -----------------------------
# Load the dataset
# -----------------------------
medical_df = pd.read_csv('medical.csv')

# -----------------------------
# Display basic statistics for the 'age' column
# Shows count, mean, std, min, percentiles, max
# -----------------------------
print(medical_df['age'].describe())

# -----------------------------
# Create an interactive histogram for the 'age' column
# Adds a box plot below for additional distribution insight
# -----------------------------
fig = px.histogram(
    medical_df, 
    x='age', 
    marginal='box',  
    nbins=47,        # one bin per age value
    title='Distribution of Age'
)
fig.update_layout(bargap=0.1)  # reduce gap between bars
# fig.show()  # Uncomment to display plot in browser

# -----------------------------
# Create an interactive histogram for the 'BMI' column
# Visualizes Body Mass Index distribution
# -----------------------------
fig = px.histogram(
    medical_df, 
    x='bmi', 
    marginal='box', 
    color_discrete_sequence=['red'], 
    title='Distribution of BMI (Body Mass Index)'
)
fig.update_layout(bargap=0.1)
# fig.show()

# -----------------------------
# Create an interactive histogram for the 'charges' column
# Color by 'smoker' to show how smoking affects medical charges
# -----------------------------
fig = px.histogram(
    medical_df, 
    x='charges', 
    marginal='box', 
    color='smoker', 
    color_discrete_sequence=['green', 'grey'], 
    title='Annual Medical Charges'
)
fig.update_layout(bargap=0.1)
# fig.show()

# -----------------------------
# Count number of smokers vs non-smokers
# -----------------------------
print(medical_df.smoker.value_counts())

# Create an interactive histogram for smokers by sex
fig = px.histogram(
    medical_df, 
    x='smoker', 
    color='sex', 
    title='Smoker Distribution by Sex'
)
# fig.show()

# -----------------------------
# Scatter plot: Age vs. Charges
# Visualizes correlation between age and medical charges
# Colors by smoker status and adds hover info for sex
# -----------------------------
fig = px.scatter(
    medical_df, 
    x='age', 
    y='charges', 
    color='smoker', 
    opacity=0.8, 
    hover_data=['sex'], 
    title='Age vs. Charges'
)
fig.update_traces(marker_size=5)
# fig.show()

# -----------------------------
# Scatter plot: BMI vs. Charges
# Shows relationship between BMI and medical charges
# -----------------------------
fig = px.scatter(
    medical_df, 
    x='bmi', 
    y='charges', 
    color='smoker', 
    opacity=0.8, 
    hover_data=['sex'], 
    title='BMI vs. Charges'
)
fig.update_traces(marker_size=5)
# fig.show()

# -----------------------------
# Correlation analysis
# -----------------------------
# Correlation between 'age' and 'charges'
age_charge_corr = medical_df['age'].corr(medical_df['charges'])
print(f"Correlation between Age and Charges: {age_charge_corr:.2f}")

# Convert smoker status to numeric: 'no' -> 0, 'yes' -> 1
smoker_numeric = medical_df.smoker.map({'no': 0, 'yes': 1})

# Correlation between smoker status and charges
smoker_charge_corr = medical_df.charges.corr(smoker_numeric)
print(f"Correlation between Smoker status and Charges: {smoker_charge_corr:.2f}")

# Correlation matrix for all numeric columns
print("Correlation matrix for numeric columns:")
print(medical_df.select_dtypes(include='number').corr())
