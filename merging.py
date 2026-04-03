import pandas as pd 
customer_data =pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ['Ramessh', 'Suresh','Kalpesh']
})

Order_data = pd.DataFrame({
    "CustomerID": [1,2,4],
    "Order Amount": [250,350,550]
})

df_merged = pd.merge(customer_data,Order_data,on="CustomerID",how="left")
print("left Join")
print(df_merged)
