import pandas as pd

data=[1,2,3,4]
df=pd.DataFrame(data)
print(df)

data1 = [['Alex',10],['Deepa',12],['Divya',34]]
df1 = pd.DataFrame(data1,columns=['Name','Age'],dtype=int)
print(df1)

####

df =pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df1 =pd.DataFrame([[5,6],[7,8]],columns=['a','b'])


df = df.append(df1)
print(df)

#df = df.drop(0)

#print(df)

for icol in df:
    print(icol)

#########

df3 = pd.DataFrame({'name':['deepa','divya','pooja','arun'], 'age':[21,31,12,34]})   
print(df3) 

for  data in df3.itertuples():
    print(data)

s= pd.Series(['deepa', 12, 34, 'sejal'])
print(s.str.len())


print(len(df3))