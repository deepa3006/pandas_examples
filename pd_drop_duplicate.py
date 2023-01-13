import pandas as pd

#DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)[source
 #--Return DataFrame with duplicate rows removed.
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]})
print (df)    


#print(df.drop_duplicates(subset=['brand','style','rating']))
#print(df.drop_duplicates(subset=['brand','style'],keep='last'))
#print(df.drop_duplicates(ignore_index=True))
print(df.drop_duplicates(subset=['brand'],keep='last',ignore_index=True))
