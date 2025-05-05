import pandas as pd
#avg,sum,max,min,sort
#sort_values(by="colname",ascending=True/False,inplace=True)

data={
    "time":[1,2,10,6,9],
    "value":[10,None,40,60,90]
}
df=pd.DataFrame(data)
# print(df)
#asc=true and desc= false
df.sort_values(by="time",ascending=True,inplace=True)
#lets also sort the value column
# df.sort_values(by="value",ascending=True)
#lets interpolate the value by placing the means
df["value"]=df["value"].interpolate(method="linear")
print(df)

#record of vk from last 5 years lets go