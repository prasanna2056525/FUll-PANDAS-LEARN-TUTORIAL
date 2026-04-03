import pandas as pd 
df = pd.read_json("sample_Data.json")

print(" Display first 10 rows")
print(df.head(10))

print ( " Display last 8 rows")
print(df.tail(8))