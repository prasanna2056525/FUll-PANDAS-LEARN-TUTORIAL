import pandas as pd 
data ={
    "Namr": ['ram', 'arun', 'hari'],
    "Age": [65,73,59],
    "Salary":[55000,40000,30000]
}
df=pd.DataFrame(data)
print(df)
print("After Sorting")

df.sort_values(by="Age", ascending=True, inplace=True)

print(df)


