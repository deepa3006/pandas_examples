import pandas as pd

#DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)[source
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

df_fortune= pd.read_csv('C:\\Users\\DEPAL6\\Downloads\\employees.csv')
print (df_fortune.columns)
df_fortune.drop_duplicates(inplace=True)
df_fortune.sort_values(by=['EMPLOYEE_ID'], ascending=[True],inplace=True)
df_fortune.to_csv('C:\\Users\\DEPAL6\\Downloads\\employee3.csv', index=False)

