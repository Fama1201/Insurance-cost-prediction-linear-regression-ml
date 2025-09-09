from urllib.request import urlretrieve
import pandas as pd

# # 1. Download the data
#
# medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
# urlretrieve(medical_charges_url, 'medical.csv')
# print("File downloaded successfully ✅")


# 2. Load the CSV using Pandas
medical_df = pd.read_csv('medical.csv')

# 3. Display the first few rows
# print(medical_df.head())

# 4. Show a statistical summary of the DataFrame
# This prints descriptive statistics for numeric columns:
# - count: number of non-null values
# - mean: average
# - std: standard deviation
# - min: minimum value
# - 25%, 50%, 75%: percentiles
# - max: maximum value
print(medical_df.describe())
