import pandas as pd

df_dept=pd.read_csv('C:\\Users\\DEPAL6\\Downloads\\departments.csv')
print(df_dept.head())
df_employees=pd.read_csv('C:\\Users\\DEPAL6\\Downloads\\employees.csv')
print(df_employees.head())


new_df = pd.merge(df_dept, df_employees,  how='inner', left_on=['DEPARTMENT_ID'], right_on = ['DEPARTMENT_ID'])
print(new_df)