import pandas as pd

bond = pd.read_csv("jamesbond.csv")
print(bond.head(3))


print("----------------------------.set_index() and .reset_index() methods-------------")
bond.set_index("Film", inplace = True)   # create index but other column are empty
print(bond.head(3))

bond.reset_index(drop = False)
print(bond.head(3))


bond.reset_index(drop = True)
print(bond.head(3))

bond.reset_index(drop = False, inplace= True)
print(bond.head(3))

"""
first need to reset_index then make set_index unless set_index remove current index and replace by new
"""

bond.reset_index(inplace= True)
bond.set_index("Year", inplace = True)
print(bond.head(3))


print("----------------------------Retrive Rows by Index Label with .loc[] and .iloc[]-------------")
# .loc[]  work with label and .iloc[] work with index . otherwise both are same
print(bond.loc[14])
print(bond.iloc[14])

# if index is string then use .iloc[] as 
bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

print(bond.loc["Casino Royale"])
print(bond.iloc[1:3])
print(bond.iloc[[0,3]])


print("----------------------------The catch-ALL .ix[] Method-------------")
# .ix[] work same as .loc[] or .iloc[]
bond.ix["GoldenEye"]
bond.ix["A View to a Kill" : "The World Is Not Enough"]
bond.ix[10:16]

#if give single unknown value then face error
#bond.ix["Sacred Bond"]


"Spectre" in bond.index
"Sacred Bond" in bond.index




print("--------------------- Second Argument to .loc[], .iloc[], and .ix[] Methods -------------")
# .loc[row,column]
bond.loc["Moonraker"]
bond.loc["Moonraker", "Actor"]
bond.loc["Moonraker", "Actor" : "Budget"]
bond.loc["Moonraker", ["Actor" ,"Budget"]]


bond.iloc[1]
bond.iloc[1, 1]
bond.iloc[1, 1:6]
bond.iloc[1, [1 ,6]]



bond.ix[5,3]
bond.ix[1, "Actor"]
bond.ix["Casino Royale", 1:6]
bond.ix[1, ["Actor" ,"Budget"]]




print("--------------------- Set New Values for a Specific Cell or Row -------------")
bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

print(bond.ix["Dr. No"])
bond.ix["Dr. No", "Actor"] = "Sir Sean Connery"
print(bond.loc["Dr. No"])

bond.ix["Dr. No", ["Box Office", "Budget", "Bond Actor Salary"]] = [448800000, 7000000, 600000]
print(bond.loc["Dr. No"])




print("--------------------- Set Multiple Values in DataFrame -------------")
bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

mask = bond["Actor"] == "Sean Connery"
df2 = bond[mask]
print(df2)

df2["Actor"] = "Sir Sean Connery"
print(df2)

# or 
bond.ix[mask,"Actor"] = "Sir Sean Connery"
print(bond)

bond[bond["Actor"] == "Roger Moore"]




print("--------------------- Rename Index Labels or Columns in a DataFrame -------------")
bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

# rename column
bond.rename(columns = {"Year": "Release Date", "Box Office": "Revenue"}, inplace = True)
print(bond.head(1))

# rename index
bond.rename(index = {"Dr. No": "Doctor No", 
                     "GoldenEye": "Golden Eye",
                     "The World Is Not Enough": "Best Bond Movie"}, inplace = True)

print(bond.head(10))
bond.ix["Best Bond Movie"]

# or we can change columns name by
bond.columns = ["Year", "Hero", "Director", "Gross", "cost", "salary"]
print(bond.head(3))




print("--------------------- Delete Rows or Columns in a DataFrame -------------")
bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

# drop rows
bond.drop("Casino Royale",inplace = False)
print(bond.head(3))

# drop columns
bond.drop(labels = ["Hero", "Director"], axis= "columns",inplace = False)

# cut columns and insert to another variable
actor = bond.pop("Hero")
print(actor)

# delete column permanentlly by del keyword
del bond["Director"]
print(bond.head(3))




print("--------------------- Create Random Sample -------------")

bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond)

bond.sample(n = 6)  # give 6 random rows from bond

bond.sample(frac = .25) # give 25% of number from bond 

bond.sample(n = 3, axis = "columns") # give 3 random columns from bond




print("--------------------- The .nsmallest() and .nlargest() methods -------------")
bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond)

# we can sort by
bond.sort_values("Year", ascending = False).head(3)
# or using .nlargest()
bond.nlargest(n=3, columns = "Year")


# we can sort by
bond.sort_values("Year", ascending = True).head(3)
# or using .nlargest()
bond.nsmallest(n=3, columns = "Year")
#or
bond["Year"].nsmallest(2)






print("--------------------- Filtering with the where Method -------------")

bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

mask = bond["Actor"] == "Sean Connery"
bond[mask]

b = bond.where(mask)

# same as
b2 = bond.where(bond["Box Office"] > 800)

b3 = bond.where(bond["Year"] > 2000)

# now
# bond.where(b3 & b2)






print("--------------------- The .query() method ------------")

bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

# using list comprehention replace data by
bond.columns = [column_name.replace(" ", "_") for column_name in bond.columns]
bond.head(1)

# using .query()
bond.query("Actor == 'Sean Connery'")

ad = bond.query("Actor == 'Sean Connery' or Director == 'John Glen'")




print("--------------------- .apply() Method on Single Columns ------------")

bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

def convert_to_String_and_add_millions(number):
    return str(number) + "MILLIONS"

bond["Box Office"] = bond["Box Office"].apply(convert_to_String_and_add_millions)

# convert multiple rows with specific value by
columns = ["Budget","Bond Actor Salary"]
for col in columns:
    bond[col] = bond[col].apply(convert_to_String_and_add_millions)





print("---------------------  .apply() Method with Row Values ------------")

bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

def good_movie(row):
    
    actor = row[1]
    budget = row[4]
    
    if actor == "Pierce Brosnan":
        return "The Best"
    elif actor == "Roger Moore" and budget > 40:
        return "Enjoyable"
    else:
        return "I have no clue"

bond.apply(good_movie, axis = "columns")





print("---------------------  .copy() Method ------------")

bond = pd.read_csv("jamesbond.csv", index_col ="Film")
bond.sort_index(inplace = True)
print(bond.head(3))

directors = bond["Director"].copy()
directors.head(3)











