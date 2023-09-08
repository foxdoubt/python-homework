import pandas as pd

df = pd.read_csv('github-course-data.csv')

first_and_last_names = df[['firstname', 'lastname']]

print(first_and_last_names)
