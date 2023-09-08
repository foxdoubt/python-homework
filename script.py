import pandas as pd

df = pd.read_csv('github-course-data.csv')

first_and_last_names = df[['firstname', 'lastname']]
info = df.info()

print(info)
print(first_and_last_names)
