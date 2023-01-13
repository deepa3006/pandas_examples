import pandas as pd 

#DataFrame.filter(items=None, like=None, regex=None, axis=None)
#DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise'
   #Drop specified labels from rows or columns.


df_employee = pd.read_csv("C:\\Users\\DEPAL6\\Downloads\\employees.csv")

#print(df_employee.filter(['EMPLOYEE_NAME','FIRST_NAME','LAST_NAME']))
df_employee=df_employee.filter(regex="(EMPLOYEE_ID|NAME$|EMAIL|^PHONE|DEPARTMENT_ID)")
print(df_employee)

# df_employee=df_employee.set_index('EMPLOYEE_ID')
# print(df_employee)

# df_employee=df_employee.reset_index(drop=True)
# print(df_employee)

df_employee=df_employee.iloc[:,[0,1,2,3,4]]
print(df_employee.columns)

df_employee=df_employee.drop('EMAIL',axis=1)
print(df_employee.columns)

print("#######Read department file#########")

df_departments = pd.read_csv("C:\\Users\\DEPAL6\\Downloads\\departments.csv")
print(df_departments.columns)
col_to_drop=df_departments.columns[2:3]
df_departments=df_departments.drop(columns=col_to_drop)
print(df_departments)

df_departments.drop('LOCATION_ID',axis=1,inplace=True)
print (df_departments.columns)