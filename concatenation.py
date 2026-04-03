#concanate vertically
import pandas as pd 
df_region1= pd.DataFrame({
    "CustomerID":[1,2],
    "Name": ["hari",'Ram']
})
df_region2= pd.DataFrame({
    "CustomerID":[3,4],
    "Name": ["shay,",'hanuman']
})
df_concate= pd.concat([df_region1,df_region2], axis=0, ignore_index=True)
print(df_concate)