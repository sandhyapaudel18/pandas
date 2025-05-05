import pandas as pd

datas={
 "time":[23,None,34,12],
 "salary":[3400,900,870,456]
}

df=pd.DataFrame(datas)
df_sum=df["time"].sum()
df_avg=df["salary"].sum()
df_st=df["time"].std()
df_count=df["time"].count()

# print(df_sum)
# print(df_avg)
# print(df_st)
print(df_count)
print(df["time"].max())

