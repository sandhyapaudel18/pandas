
"""
Nan= not a number
None= for object dtype

isnull()=true=missing else false=not missing

"""
import pandas as pd
employee={
    "name":["akash",None,"virat","ashu","bikash"],
    "age":[10,50,90,89,None],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,670,None,500,2300],
    "performance_score":[34,57,90,None,100]
}
df=pd.DataFrame(employee)
#.sum()=returns count of missing values
# print(df.isnull().sum())

#lets handle missing values
#some times drop row or column dropna(axis,inplace=True)
# df.dropna(axis=0,inplace=True)
df.dropna(axis=1,inplace=True)
print(df)


