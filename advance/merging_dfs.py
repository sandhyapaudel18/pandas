import pandas as pd
data1= {
    "name":["sandhya","akash","virat","rakesh"],
    "age":[1,4,3,2]
}  

df1=pd.DataFrame(data1)

data2={
    
    "age":[1,4,3,5],
    "weight":[19,90,80,55]
}
df2=pd.DataFrame(data2)

#inner=having same values in same cols
# df3=pd.merge(df1,df2,on="age",how="inner")
#left=common + left all
# df3=pd.merge(df1,df2,on="age",how="left")
#rigth=common+right all
# df3=pd.merge(df1,df2,on="age",how="right")
#outer=all but not havinf value is nan
# df3=pd.merge(df1,df2,on="age",how="outer")
#cross= n * m
df3=pd.merge(df1,df2,on="age",how="cross")
print(df3)