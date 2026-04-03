import pandas as pd 

data = {
    "Name": [ 'Ram', ' shyam',' ghanshyam'],
    "Age": [ 10,20,30],
    "City": [ 'Pokhara', 'Kathmandu', ' Jhapa']
}
df=pd.DataFrame(data)
print(df)
#df.to_csv("output.csv", index="False")
#df.to_excel("output.xlsx")
df.to_json("output.json")