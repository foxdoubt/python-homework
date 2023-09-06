import pandas as pd

data = pd.read_csv('github-course-data.csv')

firstnames = data['firstname'].values
lastnames = data['lastname'].values
emails = data['email'].values

print(firstnames)
print(lastnames)
print(emails)
