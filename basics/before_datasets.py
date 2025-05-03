import pandas as pd
df=pd.read_excel("students.xlsx")

#gcsfs for google cloud data

#understand the data sets, types, identity problems and find missing,duplicated and mistaken datas
#plan next steps

# s methods = head and tail
#head(n) =shows n no of rowsfrom beginning
#tail(n)= shows n no of rows from last


# print(df.head(3)) #first 3 values
# print(df.tail(2)) #last 2 values

#if no value then default 5
#columns,rows
#types of datas
#missing data locations
#info() = no of rows and columns alsowith name and datatypes also not null count
print("Displaying infos of datasets")
print(df.info())
