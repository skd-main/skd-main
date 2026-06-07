import pandas as pd
df = pd.read_csv('data/ukri_projects_raw.csv')
print(df.shape)
print(df.columns)
print("-------------------------------------------------------------------------")
print(df.isnull().sum())
print(df['AwardPounds'].describe())