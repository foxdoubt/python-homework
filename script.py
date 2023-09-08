import pandas as pd

df = pd.read_csv('github-course-data.csv')

first_and_last_names = df[['firstname', 'lastname']]

condition_1 = df['profession'] == 'developer'
condition_2 = df['profession'] == 'firefighter'

print(df[condition_1 | condition_2])
print(first_and_last_names)
