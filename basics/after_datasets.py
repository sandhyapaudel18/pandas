import pandas as pd
data={
    "name":["sandhya","akash","virat"],
    "age":[10,20,70],
    "city":["sunwal","delhi","newroad"]
}
df=pd.DataFrame(data)
print(df)

#dataframe to csv after manipulation
#index=false no indexing
# df.to_csv("output.csv",index=False)
df.to_excel("newdata.xlsx",index=False)  