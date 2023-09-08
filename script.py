import pandas as pd

df = pd.read_csv('github-course-data.csv')

first_and_last_names = ['firstname','lastname']

print(df[first_and_last_names].to_string())