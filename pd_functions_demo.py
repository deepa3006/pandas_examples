import pandas as pd
import os

#DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# Remove missing values

df_employee = pd.read_csv("C:\\Users\\DEPAL6\\Downloads\\employees.csv")
#print(df_employee.shape)
#print(df_employee.columns)
df_employee_orig=df_employee.copy()
# print (df_employee.head(5))
# print (df_employee.nunique())
df_employee.dropna(subset=['FIRST_NAME','LAST_NAME'],how='all')
print(df_employee)

df_employee_new=df_employee.dropna(subset=['FIRST_NAME','LAST_NAME'],how='all')
print (df_employee_new)

#df_employee['FIRST_NAME'].fillna("deepa",inplace=True)
#print(df_employee)