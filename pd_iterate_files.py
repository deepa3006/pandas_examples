import pandas as pd
import numpy as np


#list_of_datasets=[df_a,df_b]
#for df, df1 in enumerate(list_of_datasets): 



# def max_common(df_a, df_b): 
#     for i in range(len(df_a.index)): 
#         for j in range(len(df_a.columns)):
#             df_c.iloc[i,j] = np.where(df_a.iloc[i,j]>=df_b.iloc[i,j], df_a.iloc[i,j], df_b.iloc[i,j])
#     df_c.columns=df_a.columns      
#     return df_c

   

df_a = pd.DataFrame([[16, 2, 30], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
df_b = pd.DataFrame([[10,5,60,2], [11, 34, 2,30], [100, 300, 200,76]],columns=['D', 'B', 'C','A'])
df_c=pd.DataFrame()

for col in df_a.columns:
    df_c[col]=df_a[col]

    for col1 in df_b.columns:
        if(col==col1):
            df_c[col]=np.where(df_a[col]>=df_b[col1], df_a[col], df_b[col1])
            #print(df_c)
            break
#df_c[col]=df_a[col]
print(df_c)        
            

# df_out= max_common(df_a,df_b)
# print(df_out)