import pandas as pd

df = pd.read_csv('github-course-data.csv')
info = df.info()
print(info)