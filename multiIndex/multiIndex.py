import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"])
bigmac.head(3)





print("----------------------Create A MultiIndex with the .set_index() Method-----------------------")

bigmac.set_index(keys = ["Date","Country"], inplace = True)  # work with respected Index data as mach as a layer keys=[Index1,Index2]
bigmac.head(3)

bigmac.sort_index() # sort data in alpha numaric. here Now Date Is 1st index, country is 2nd index


# see name of Index by
bigmac.index.names
bigmac.index.names[0]


# we can see its type as multindex by
type(bigmac.index)






print("---------------------The .get_level_values() Method-----------------------")

import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)

# we can see all index by
bigmac.index
bigmac.index[0]

# we can see the value of our index by
bigmac.index.get_level_values(1)
bigmac.index.get_level_values("Date")





print("---------------------The .set_names() Method-----------------------")

import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# We can change our Index Name By set new index name as
bigmac.index.set_names(["Day", "Location"], inplace = True)
bigmac.head(3)






print("---------------------The .sort_index() Method-----------------------")

import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)


# we can sort all as ascending/discending or can be sort specific order in maltiIndex as
bigmac.sort_index(ascending = [True, False], inplace = True) # we sort Date ascending and Country Descending








print("---------------------Extract Rows from a MultiIndex DataFrame using .loc(), .ix()-----------------------")

import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)

# loc accept index level
bigmac.loc[("2010-01-01")]
bigmac.loc[("2010-01-01","China")]
bigmac.loc[("2010-01-01","China"), "Price in US Dollars"] # if we have more column we can be define after index tuple

# same bu using .ix()
bigmac.ix[("2010-01-01","China")] 
bigmac.ix[("2010-01-01","China"), 0] # if we have more column we can be define after index tuple









print("---------------------The .transpose() Method-----------------------")

import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)

# replace rows to columns and columns to row
bigmac = bigmac.transpose()
bigmac.head(3)

bigmac.ix["Price in US Dollars", ("2016-01-01", "Denmark")]











print("---------------------The .swaplevel() Method-----------------------")

import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
bigmac.head(3)

# if your index have more than 2 level then need to swap by
bigmac = bigmac.swaplevel() # no inplace parameter, need to declar as bigmac = bigmac.swaplevel()
bigmac.head(3)








print("---------------------The .stack() Method-----------------------")

import pandas as pd

world = pd.read_csv("worldstats.csv",index_col = ["country","year"])
world.head(3)

# display total value for a specific multiIndex by 
a = world.stack()
type(world.stack()) # its a series 

# we can convert series to dataFrame by .to_frame()
a.to_frame()









print("---------------------The .unstack() Method-----------------------")

# unstack besically reverse of stack method
a.unstack() # its unstack our created stack


b = a.unstack().unstack() # its change our multi layer's inner Index as column 


c = a.unstack().unstack().unstack()  # its make data frame to series





import pandas as pd

world = pd.read_csv("worldstats.csv",index_col = ["country","year"])
world.head(3)

a = world.stack()
a
a.unstack(2)  # unstack 3 number column (Population,GDP)
a.unstack(0)  # unstack 1 number column (country )
a.unstack(-1)  # unstack last number column 

a.unstack("country")  # unstack 1 number column (country )

# we can unstack column as new levels 
a.unstack(level = ["country", "year"])

s1 = a.unstack("year")
# we can fill NaN value with 0 or specific value by
s = a.unstack("year", fill_value = 0)








print("---------------------The .pivot() Method-----------------------")

import pandas as pd

sales = pd.read_csv("salesmen.csv",parse_dates = ["Date"])
sales["Salesman"] = sales["Salesman"].astype("category")
sales.head(3)

# we can specifi all levels data to needed catagory by .pivot()
sales.pivot(index = "Date", columns = "Salesman", values = "Revenue")







print("---------------------The .pivot_table() Method-----------------------")

import pandas as pd

foods = pd.read_csv("foods.csv")
foods.head(3)

# work like microsoft xl by .pivot_table
foods.pivot_table(values = "Spend", index = "Gender", aggfunc = "min")

# work with multiIndex
foods.pivot_table(values = "Spend", index = ["Gender","Item"], aggfunc = "max")

# for specific colums 
foods.pivot_table(values = "Spend", index = ["Gender","Item"],columns = "City", aggfunc = "sum")






print("---------------------The pd.melt() Method-----------------------")

import pandas as pd

sales = pd.read_csv("quarters.csv")
sales  

pd.melt(sales, id_vars = "Salesman")

# give variable_name and value_name
pd.melt(sales, id_vars = "Salesman", var_name = "Quarter", value_name = "Revenue")






