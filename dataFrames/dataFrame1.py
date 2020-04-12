import pandas as pd

cm = pd.read_csv("Churn_Modelling.csv",squeeze = True)

print(cm.head(20))


print("------------------- Shared Methods and Attributes------------------")

print("display all columns:\t", cm.columns,"\n")
print("display all index:\t", cm.index,"\n")
print("total index length:\t", len(cm.index),"\n")
print("total columns length:\t", len(cm.columns),"\n")

print("Rows, Columns:\t", cm.shape)
print("DataType:\n", cm.dtypes)

print("Rows, Columns:\n", cm.axes)   # RangeIndex is  row , Index([colunms]) is Columns

print("Summery:\n", cm.info())  # most usefull......................................

#print("total data type\t", cm.get_dtype_counts())

# only work with dataFrame not for serires
print(cm.sum(0)) # 0 means row 
print(cm.sum(1)) # 1 means row 





print("------------------- Select one column from a dataFrame------------------")

print(cm.Balance) # convert to a series
# or
print(cm["Balance"].head())
print(type(cm["Balance"]))
print(type(cm.Balance))







print("------------------- Select two or more columns from a dataFrame------------------")

print(cm[["Surname","Balance"]].head())
print(type(cm[["Surname","Balance"]]))







print("------------------- Add a new column to DataFrame------------------")
cm["new_row"] = "New value"
print(cm)

cm.insert(1, column = "NewC", value = "NewC Value")
print(cm)


cm = pd.read_csv("Churn_Modelling.csv",squeeze = True)

print(cm.head(20))








print("------------------- Broadcasting Operations ------------------")

print(cm["CustomerId"].add(10).head())
# or
print(cm["CustomerId"]+ 10)


print(cm["CustomerId"].sub(10).head())
# or
print(cm["CustomerId"]- 10)


print(cm["CustomerId"].mul(10).head())
# or
cm["CustomerId_New"] = cm["CustomerId"]* 10
print(cm["CustomerId_New"].head())
print(cm.head())


cm["CustomerId_New"] = cm["CustomerId"].div(1000000)
print(cm.head())






print("------------------- .value_counts() ------------------")

print(cm["Gender"].value_counts())
print(cm['Exited'].value_counts())










print("------------------- Drop Rows with Null Values ------------------")
#  axis =0= Row, axis=1=Column

salary = pd.read_csv("salary.csv")
print(salary)
print(salary.dropna()) # remove full rows if any null values happend

# remove those row whoes all value are null
print(salary.dropna(how = "all"))

# remove those row whoes all value are null and replace permanently
print(salary.dropna(how = "all", inplace = True))

#check specific column , if any null in specific column then drop thoes row care by specific column
print(salary.dropna(subset = ["Salary"]))

print(salary)

print("------------------- Drop Columns with Null Values ------------------")

salary["new"]= 0.00  # can't make null value so can't be drop
print(salary)
print(salary.get_dtype_counts())

print(salary.dropna(axis = 1)) # remove full Column if any null values happend

# can be apply all Drop row to drop column just change by "axis = 1"








print("------------------- Fill Null Values with the .fillna() method------------------")
# replace all Null value with specific value
print(salary.fillna(0))

# replace specific column's all Null value with specific value
print(salary["Salary"].fillna(value = "Here we found null value", inplace = False))






print("------------------- .astype() method------------------")
salary["new"] = salary["new"].astype("int")
print(salary["new"])






print("------------------- .numique() method------------------")
# use to find total different type of value
print(salary["Purchased"].nunique())
print(salary)


# reduse memory space.............................by change astype

salary["Salary"] = salary["Salary"].astype("int")
print(salary)
print(salary.info())



#  example to reduse memory size
print(salary["Country"].nunique())
print(salary["Country"].astype("category"))
print(salary.info())





print("------------------- Soer a DataFrame th the .sort_value()  method------------------")
print(salary)
print(salary.sort_values("Country"))

print(salary.sort_values("Country", ascending = False, inplace = False))

# sort with Null value na_position = "last", seen null value top 

print(salary.sort_values("Country", na_position = "first"))  # or na_position = "last"













