import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")

len(week1)    # same length
len(week2)




print("--------------- the pd.concat() method--------------------")

wek1and2 = pd.concat([week1, week2], ignore_index = True)


sales = pd.concat([week1, week2], keys= ["week1", "week2"])

sales.ix["week1"]

sales.ix[("week2", 240)]

sales.ix[("week2", 240), "Customer ID"]







print("--------------- the .append() method--------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")

week1_2 = week2.append(week1, ignore_index = True)  # work same as concat method









print("--------------- inner Joins (inner marge)--------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")

""" try to find which customer are came on week1 and week2 both """

# both dataset have same name of column "Customer ID" so it defaultly create "Customer ID_x""Customer ID_y" for reduse duplicate column name
week1.merge(week2, how = "inner", on = "Customer ID").head(4)


# now give some specific name to "Customer ID"
week1.merge(week2, how = "inner", on = "Customer ID",suffixes = [" - week 1"," - week 2"]).head(4)



""" try to find which customer are came on both week1 and week2 both and ordered exjact same product to both week1 & week2"""
week1.merge(week2, how = "inner", on = ["Customer ID", "Food ID"]).head(4)










print("--------------- outer Joins (outer marge)--------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")

""" try to find which customer are not came on week1 and week2 both """

# both dataset have same name of column "Customer ID" so it defaultly create "Customer ID_x""Customer ID_y" for reduse duplicate column name
week1.merge(week2, how = "outer", on = "Customer ID").head(4)

# NaN found when those costomer is not found in column
# now give some specific name to "Customer ID".  indicator parameter define where the value is
marged = week1.merge(week2, how = "outer", on = "Customer ID",
                     suffixes = [" - week 1"," - week 2"], indicator = True)

len(marged)  # 454 rows have not similar value 


""" try to find which customer are not came on both week1 and week2 both and ordered exjact same product to both week1 & week2"""
week1.merge(week2, how = "outer", on = ["Customer ID", "Food ID"]).head(4)


# total discription
marged["_merge"].value_counts()









print("--------------- left Joins (left marge)--------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")


""" try to find which food item buy customer on week1 """ # so food ID is our matching column
buy = week1.merge(food, how = "left", on = "Food ID", sort = True) # it's sort with matching column
buy.head()






print("--------------- right Joins (left marge)--------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")


""" try to find which food item buy customer on week1 """ # so food ID is our matching column
buy = food.merge(week1, how = "right", on = "Food ID", sort = True) # it's sort with matching column
buy.head()









""" 
When marged column have not same name then we cann't work with previous marge or join system.
matching or comparing columns always need same name. If that's not happend then we need extra 2 parameter left_on & right_on
"""

print("--------------- left_on and right_on parameters --------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food = pd.read_csv("Restaurant - Foods.csv")

week2.merge(customers, how = "left", left_on = "Customer ID", right_on = "ID") # "Customer ID" & "ID" same so we don't need duplicate column
 
week2CustomerDemo = week2.merge(customers, how = "left", left_on = "Customer ID", right_on = "ID", sort = True).drop("ID", axis= "columns")  # now ID column is drop
week2CustomerDemo.head()









print("--------------- Merging by Indexes with the left_index and right_index Parameters --------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv", index_col = "ID")  # define index column cause data frame have extra number column serial
food = pd.read_csv("Restaurant - Foods.csv",  index_col = "Food ID")

food.head()


""" 
use for marge with index value or marge with index and column
"""
sales = week1.merge(customers, how = "left", left_on = "Customer ID", right_index = True)

# now marge with foods data set to add food details with sales 

sales.merge(food, how = "left", left_on = "Food ID", right_index = True)
sales.head()


# merge by Index In both datasets
week1.merge(week2, how = "left", left_index = True, right_index = True, suffixes = ["-week1", "-week2"])










print("--------------- The .join() Method --------------------")
import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv", index_col = "ID")  # define index column cause data frame have extra number column serial
food = pd.read_csv("Restaurant - Foods.csv",  index_col = "Food ID")
satisfaction = pd.read_csv("Restaurant - Week 1 Satisfaction.csv")

# use for join 2 dataSet with out extra parameter
week1.join(satisfaction).head()










print("--------------- The .merge() Method --------------------")

import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv", index_col = "ID")  # define index column cause data frame have extra number column serial
food = pd.read_csv("Restaurant - Foods.csv",  index_col = "Food ID")
satisfaction = pd.read_csv("Restaurant - Week 1 Satisfaction.csv")


pd.merge(week1, customers, how = "left", left_on = "Customer ID", right_on = "ID").head()







































