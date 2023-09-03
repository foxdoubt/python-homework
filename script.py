import pandas as pd

data = pd.read_csv('github-course-data.csv')

firstnames = data['firstname'].values

print(firstnames)