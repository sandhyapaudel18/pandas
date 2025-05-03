#finding missing values ma estimated value
# 10,20,NaN,40,50
#for numerical columns linear=> preserve data integrity and smooth predictions also avoids data loss
#,polynomial 

#interpolate() estimate nikalcha by comparing with other data 
#linear,polynomial,time
import pandas as pd
employee={
    "name":["akash",None,"virat","ashu","bikash"],
    "age":[10,50,None,89,30],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,None,400,500,2300],
    "performance_score":[34,57,90,89,None]
}
df=pd.DataFrame(employee)
df.interpolate(method="linear",axis=0,inplace=True)
print(df)
