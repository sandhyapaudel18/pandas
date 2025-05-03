import pandas as pd
employee={
    "name":["akash","sandhya","virat","ashu","bikash"],
    "age":[10,50,90,89,30],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,670,400,500,2300],
    "performance_score":[34,57,90,89,100]
}
df=pd.DataFrame(employee)
#.loc[row_index,col_name]=new_value access and update
#lets update name osandhya to vikash
updated_name=df.loc[1,"name"]="vikash"
# print(df)
#all  updation at once
df["salary"] += df["salary"]*0.5 
print(df)