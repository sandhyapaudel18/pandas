import pandas as pd

datas={
 "time":[23,44,34,12],
 "salary":[3400,900,870,456]
}

df=pd.DataFrame(datas)
df_sum=df["time"].sum()
df_avg=df["salary"].sum()
df_st=df["time"].std()

print(df_sum)
print(df_avg)
print(df_st)

