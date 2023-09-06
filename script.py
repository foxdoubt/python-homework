import pandas as pd

data = pd.read_csv('github-course-data.csv')

firstnames = data['firstname'].values
lastnames = data['lastname'].values

print(firstnames)
print(lastnames)
