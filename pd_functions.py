import pandas as pd
import numpy as np

df = pd.DataFrame({'A': range(3), 'B': range(1, 4)})
df.columns=['C','D']
#print(df)




# print(df.loc[2,'C']) 
# print(df.loc[0:,'C']) 
# print("###iloc")
# print(df.iloc[2,2])  
# print(df.iloc[[2]])
# print("####at & iat")
# print(df.at[1,'C']) 
# print(df.iat[1,2])              