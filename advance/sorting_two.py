import pandas as pd
data={
    "time":[1,2,10,6,9],
    "value":[10,100,40,60,90]
}
df=pd.DataFrame(data)
#sorting multiple columns at once
#df.sort(by=["col1","col2"],ascending=True,inplace=True)

# df["value"]=df["value"].interpolate(method="linear")
df.sort_values(by=["time","value"],ascending=[True,False],inplace=True)