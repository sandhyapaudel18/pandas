#linear interpolation
#timings ko bare ma use garne interpolation
#also with numerical things
import pandas as pd
data={
    "time":[1,2,4,6,5],
    "value":[10,None,40,60,90]
}
df=pd.DataFrame(data)
print("before")
print(df)

print("after")
#df.interpolate(method="linear",axis=0,inplace=True)
df["value"]=df["value"].interpolate(method="linear")
print(df)