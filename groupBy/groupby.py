import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


len(sectors)  # gropeBy create 21 unique group
fortune["Sector"].nunique()  # we see total unique object

# we can see our total unique object with there value by .size()
sectors.size() # there are 21 sector , we see

# we can also see our unique object with its value by .value_count() but value_count make sorted as
fortune["Sector"].value_counts()  # there are 21 sector , we see


print("-----------------------Basic group object----------------")
# we can extract very first row on group by .first()
sectors.first()

# we can extract last row on group by .first()
sectors.last()

# we can represent every group as a python dictionary. each group object represent as key and values are index label as
sectors.groups

# now we see our first keys 1st value what represent by .loc[]
fortune.loc[24] # here sector which is group object, that match with 1st key







print("-----------------------Retrieve A group with the .get_group() Method----------------")

import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)

# now we extract any group object's total value as a sub set by .get_group("groupObj")
energy = sectors.get_group("Energy")
# same as
tec = sectors.get_group("Technology")


# now try to create sub-set of all group values separetly by
fortune[fortune["Sector"] == "Apparel"]  # thats create one dataframe similar as .get_group()method
 







print("-----------------------Method on the Groupby Object and DataFrame Columns----------------")

import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)

# now if we use .max() its display last alphabetcaly or max value of each group object's very first columns defaultly
sectors.max()
# same for .min() method
sectors.min()

# but for numeric operation it's just take those columns which have numeric value as
sectors.sum()
sectors.mean()

# we can also work same for specific group object by
sectors.get_group("Apparel")["Revenue"].sum()

# we can also work same for specific colums  all value on group boject by
sectors["Revenue"].sum()
sectors["Employees"].sum()
sectors["Profits"].max()
sectors[["Employees", "Profits"]].sum()







print("-----------------------Grouping By Multiple Columns----------------")

import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby(["Sector", "Industry"])
fortune.head(3)

# here we can see our created multi indexing
sectors.size()

# now try to work with multiIndex group object
sectors["Revenue"].sum()








print("-----------------------The Aggragation  .agg() Method----------------")

import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)

# now we can aggragation specific unique column by
sectors.agg({"Revenue" : ["sum","mean"],
             "Profits" : "sum",
             "Employees" : "mean"})

# or we can do same by
a = sectors.agg(["size","sum","mean"])







print("-----------------------Iterating through Groups----------------")

import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
fortune.head(3)


# we can extract every value from a group object with specific operation by

df = pd.DataFrame(columns = fortune.columns) # seen empty value with all columns

for sector, data in sectors:
    highest_revenue_company_in_group = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_company_in_group)



# or we can do same by
cities = fortune.groupby("Location")
df2 = pd.DataFrame(columns = fortune.columns)
df2  # seen empty value with all columns

for city, data in cities:
    highest_revenue_in_city = data.nlargest(1, "Revenue")
    df2 = df2.append(highest_revenue_in_city)












