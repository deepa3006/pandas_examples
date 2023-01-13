import pandas as pd
import numpy as np

#Create a Series from ndarray
data = np.array(['a','b',3,4])
s=pd.Series(data)
print(s)

s1 =pd.Series(data,index=[101,102,103,104])
print(s1)

#Create an Empty Series
s= pd.Series()
print("s =", s)

####################

#####################
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]],columns=['a','b'])

df = df.append(df2)
print ("df")
print(df)
print('\n')

#Create a Series from dict
s3 = pd.Series({'a':23, 'b':87})
print ("s3\n")
print(s3) 
