import pandas as pd
fortune = pd.read_csv("C:\\Users\\DEPAL6\\Downloads\\fortune.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
print (fortune.head())