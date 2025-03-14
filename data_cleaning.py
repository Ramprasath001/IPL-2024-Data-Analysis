# importing libraries and data cleaning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv("IPL-2024-Data-Analysis/data/ipl2024_matchs.csv")
# Display first 5 rows
df.head()
# Check for missing values
print(df.isnull().sum())
# Fill missing values with appropriate values (if needed)
df.fillna({"first_score": 0, "second_score": 0, "first_wkts": 10, "second_wkts": 10}, inplace=True)
# Remove duplicates
df.drop_duplicates(inplace=True)