"""
#data modification
add columns
update datas

"""
import pandas as pd
employee={
    "name":["akash","sandhya","virat","ashu","bikash"],
    "age":[10,50,90,89,30],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,670,400,500,2300],
    "performance_score":[34,57,90,89,100]
}
df=pd.DataFrame(employee)
# new column df["name"]=["values"]
df["weight"]=[19,80,90,45,46]
# print(df)

#another way df.insert(index,colnname,data_content)
cal_bonus=df["salary"] * 0.1
df.insert(0,"bonus",cal_bonus)
print(df)

