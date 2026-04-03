import pandas as pd 
data ={
    "Name":[ 'ram', 'shyam', 'hari', 'sita','lily', 'sashi','Raj','Prasanna'],
    "Age":[22,34,36,75,40,55,78,66],
    "Salary":[50000,10000,200000,30000,70000,800000,370000,900000],
    "Performance Index":[99,80,88,89,98,87,69,95] 
}
df=pd.DataFrame(data)
print("Sample dataset")


df.loc[0,"Salary"]=55000
print(df)