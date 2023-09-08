import pandas as pd

df = pd.read_csv('github-course-data.csv')

condition_1 = df.profession == 'worker'
condition_2 = df.profession == 'firefighter'

query_result = df[condition_1 | condition_2]
print(query_result.to_string())