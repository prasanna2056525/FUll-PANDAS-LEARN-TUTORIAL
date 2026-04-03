import pandas as pd 
data ={
    "Name":[ 'ram', 'shyam', 'hari', 'sita','lily', 'sashi','Raj','Prasanna'],
    "Age":[22,34,36,75,40,55,78,66],
    "Salary":[50000,10000,200000,30000,70000,800000,370000,900000],
    "Performance Index":[99,80,88,89,98,87,69,95] 
}
df=pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print("Names Single column selecting examples")
name=df['Name']
print(name)

subset=df[["Name","Age"]]
print(subset)

# Filtering Rows

filtered_rows= df[df["Salary"]>50000]
print(filtered_rows)
#filtering rows salary greater than 50000 and age less than 60
filtered=df[(df["Salary"]>50000) & (df["Age"]>60)]
print(filtered)
# using or function
filtered_or = df[(df["Salary"]>50000) | (df["Age"]>60)]
print(filtered_or)