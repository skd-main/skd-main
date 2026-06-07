"""
explore_ukri.py
---------------
Initial exploration of the UKRI Gateway to Research dataset.
Source: https://gtr.ukri.org/search/project?term=*
Downloaded: June 2026

Dataset: 174,405 projects, 25 columns
Key findings:
- PIOtherNames and StudentOtherNames are 100% null - drop in cleaning
- ExpenditurePounds is 99% null - drop in cleaning
- AwardPounds is heavily skewed - median £92k vs mean £411k
- ~25% of projects have £0 recorded funding
- PI and Student fields are mutually exclusive (project has one or the other)
"""

import pandas as pd

df = pd.read_csv('data/ukri_projects_raw.csv')

# ── Dataset shape ──────────────────────────────────────────────────────────────
print("SHAPE (rows, columns):")
print(df.shape)

# ── Column names ───────────────────────────────────────────────────────────────
print("\nCOLUMNS:")
print(df.columns.tolist())

# ── Missing values per column ──────────────────────────────────────────────────
print("\nMISSING VALUES:")
print(df.isnull().sum())

# ── Funding amount distribution ────────────────────────────────────────────────
print("\nAWARD POUNDS - Summary statistics:")
print(df['AwardPounds'].describe())

# ── Sample rows ────────────────────────────────────────────────────────────────
print("\nFIRST 5 ROWS:")
print(df.head())