import pandas as pd 
data ={
    "Namr": ['ram', 'arun', 'hari', 'shyam','shashi'],
    "Age": [65,73,59,65,62],
    "Salary":[55000,40000,30000,55000,45000]
}
df=pd.DataFrame(data)
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)
