import pandas as pd

df1 = pd.DataFrame([['depal6id1','4', 'C'],['arvanid2','2','R'],['mahsgid3','3','R']],columns=['playerId','score','pos'])
df2 = pd.DataFrame([['depal6id1','Deepa Palabhavi'],['arvanid2','Arun Vandal'],['mahsgid3','Misha' 'Nani']],columns=['playerId','name'])

print(pd.merge(df1,df2))

######################
df3 = pd.DataFrame([['depal6id1','4', 'C'],['arvanid2','2','R'],['mahsgid3','3','R']],columns=['playerId','score','pos'])
df4 = pd.DataFrame([['depal6id1','Deepa Palabhavi','Right wing'],['arvanid2','Arun Vandal','Center'],['mahsgid3','Misha' 'Nani','Right wing']],columns=['playerId','name','pos'])
print(pd.merge(df3,df4))

###############
print("Joining if indexes are same\n")
df5 = pd.DataFrame([['depal6id1','4'],['arvanid2','2'],['mahsgid3','3']],columns=['playerId','score'])
df6 = pd.DataFrame([['depal6id1','Deepa Palabhavi'],['arvanid2','Arun Vandal'],['mahsgid3','Misha Nani']],columns=['playerId','name'])
df7 = pd.DataFrame([['depal6id1','Right wing'],['arvanid2','Center'],['mahsgid3','Right wing']],columns=['playerId','pos'])

df5=df5.set_index('playerId',drop=True)
df6=df6.set_index('playerId',drop=True)
df7=df7.set_index('playerId',drop=True)
print(df5.join([df6,df7]))

#####################
#pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, 
# left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), 
# copy=True, indicator=False, validate=None)

df_dept=pd.read_csv('C:\\Users\\DEPAL6\\Downloads\\departments.csv')
print(df_dept.columns)
df_employees=pd.read_csv('C:\\Users\\DEPAL6\\Downloads\\employees.csv')
print(df_employees.columns)

df_join=df_employees.merge(df_dept,how='inner',left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',sort=True,suffixes=('MANAGER_ID_employee','MANAGER_ID_department'))
print(df_join.columns)