import pandas as pd
import datetime

json_str = '{"Courses":{"r1":"Spark"},"Fee":{"r1":"25000"},"Duration":{"r1":"50 Days"}}'
df = pd.read_json(json_str)
#print(df.to_string())

#df1=pd.read_json(r'C:\Users\DEPAL6\Vs-code\my-python-app\my-first-repo\people.json')
df1=pd.read_json('C:\\Users\\DEPAL6\\Downloads\\fruits_02.json')
#df1=pd.read_json('C:/Users/DEPAL6/Downloads/example.json')
df2=df1.copy()

df2['time']=datetime.datetime.now()
print(df2,"\n")
#print(df2.to_string())

#for i in df2.index:
    #if df2.loc[i,'size'] == 'small':
        #df2.loc[i,'size'] == 'SMALL'
        #df2.drop(i, inplace = True)
#print(df2)

data={'fname':['Deepa','Sejal','Arun'],'lname':['Palabhavi','Vandal','NAN']}
df3=pd.DataFrame.from_dict(data)
print(df3,"\n")


df3['flname']=df3['fname']+df3['lname']
print(df3)

#df4=pd.concat(df3['fname'], df3['lname'])
#print(df4)

# def concat_size_colour(df3):
#     for x in df3.index:
        
#         return df3

# df_concat=concat_size_colour(df3)
# print(df_concat)

data = [{'col_1': 3, 'col_2': 'a'},
        {'col_1': 2, 'col_2': 'b'},
        {'col_1': 1, 'col_2': 'c'},
        {'col_1': 0, 'col_2': 'd'}]
df5=pd.DataFrame.from_records(data)
print(df5)
 