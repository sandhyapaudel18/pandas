#data is big or small
#name of columns
#shape=no of rows and columns / attribute
#columns= name of columns

import pandas as pd
employee={
    "name":["akash","sandhya","virat","ashu","bikash"],
    "age":[10,50,90,89,30],
    "city":["sunwal","butwal","bankatti","delhi","mumbai"],
    "salary":[100,670,400,500,2300],
    "performance_score":[34,57,90,89,100]
}

df=pd.DataFrame(employee)
print(df.columns)
print(df.shape)
