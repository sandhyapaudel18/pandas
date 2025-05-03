import pandas as pd
employee={
    "name":["akash","sandhya","virat","ashu","bikash"],
    "age":[10,50,90,89,30],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,670,400,500,2300],
    "performance_score":[34,57,90,89,100]
}
df=pd.DataFrame(employee)
# print(df)
# name=df["name"]
# print(name)
# print((df["age"]>10) & (df["age"]<90))
# print(df[["name","age"]])

#rows filteringg
#single condition
high_salary=df[df["age"]>10]
# print(high_salary)

#multiple conditions
high_age_salary=df[(df["age"]>10) & (df["performance_score"]>90)]
# print(high_age_salary)

high_age_score=df[(df["age"]>35) | (df["performance_score"]>90)]
print(high_age_score)

