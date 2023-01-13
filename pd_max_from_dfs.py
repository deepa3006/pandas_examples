import pandas as pd
import numpy as np



df_a = pd.DataFrame([[16, 2, 30], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
df_b = pd.DataFrame([[10,5,60,2], [11, 34, 2,30], [100, 300, 200,76]],columns=['D', 'B', 'C','A'])
df_c=pd.DataFrame()

# for col in df_a.columns:
#     df_c[col]=df_a[col]
#     for col1 in df_b.columns:
#         if(col==col1):
#             df_c[col]=np.where(df_a[col]>=df_b[col1], df_a[col], df_b[col1])
#             break
# print(df_c)  


#Solution2#


def max_common(df_a, df_b):
    rows = [[df_a[x][y] if x not in df_b.columns else max(df_a[x][y], df_b[x][y]) for x in df_a.columns] for y in df_a.index]
    print(rows)
    return pd.DataFrame(data=rows, columns=df_a.columns)

df_c=max_common(df_a,df_b)  
print(df_c)  

#Solution3
def max_common(df_a, df_b): 
    df_new = df_a.copy()
    for column in df_b:
        if column in df_a:
            df_new[column] = df_new[column] = pd.concat([df_a[column], df_b[column]]).max(level=0)
    return df_new