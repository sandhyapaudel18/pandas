import pandas as pd
employee={
    "name":["akash",None,"virat","ashu","bikash"],
    "age":[10,50,None,89,30],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,None,400,500,2300],
    "performance_score":[34,57,90,89,None]
}
df=pd.DataFrame(employee)
#for adding some values in missing data lets handel that here
# df.fillna(0,inplace=True)
#provide mean for numerical values
df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)
print(df)