import pandas as pd
import random 
import numpy as np

# randnums= np.random.randint(0,100, size=(2,3))
# print(randnums)

# df = pd.DataFrame([[1,2,3],[4,5,6]])
# data = [[1,2,3],[4,5,6]]
# #print(df)
# print("###########")
# #df2 = pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
# df2 = pd.DataFrame(randnums,columns=['a','b','c'])
# print(df2)
# print("#############")
# # import random
# randomlist = []
# for i in range(0,3):
#     n = random.randint(1,30)
#     randomlist.append(n)
#     #print(randomlist)
# print(randomlist)

def rename_columns(df, names):  
    df2 = df.copy()
    #print(df2)
    df2.columns = names
    print(df2.values)
    return df2

df_input = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
#print(df_input)
#print(list('ABC'))
df3=rename_columns(df_input,list('ABC'))
print(df3)


df4 = pd.DataFrame(np.random.randn(2, 2))
print(df4)