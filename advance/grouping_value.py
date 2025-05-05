#splitting dataset into small groups
import pandas as pd
data={
    "name":["sandhya",None,"virat","akshu","ritesh"],
    "time":[12,35,35,89,None],
    "salary":[64,89,None,10,80]
}
df=pd.DataFrame(data)
#using grouped by to perform aggregate functions in columns if there are duplicate datas and create unique values
grouped=df.groupby("time")["salary"].sum()
grouped_multi=df.groupby(["time","name"])["salary"].sum()
print(grouped_multi)

