import pandas as pd
emply = pd.read_csv("employees.csv")

print(emply.info())
print(emply.columns)








print("----------------------- .to_dateTime---------------------------")

print(pd.to_datetime(emply["Start Date"]))
print(pd.to_datetime(emply["Last Login Time"]))

# or
df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
print(df)











print("--------------------------reduse memory---------------------")

df = pd.read_csv("employees.csv", parse_dates = ["Start Date", "Last Login Time"])
df['Senior Management'] = df['Senior Management'].astype("bool")
df['Gender'] = df['Gender'].astype("category")
print(df.head(3))
print(df.info())    # compare to emply.info()












print("---------------------filter A DataFrame Based On a Condition--------------")

df[df["Gender"] == "Male"]

# work as details
mask = df["Team"] != "Finance"
print(mask)
print(df[mask]) # print all without Finance in Team column

# or example same as
print(df[df["Salary"] > 110000])

print(df[df["Start Date"] <= "1985-01-01"])


mask1 = df["Senior Management"]
mask2 = df["Start Date"] <= "1985-01-01"

print(df[mask1 | mask2])

#or
print(df[(df["Gender"] == "Male") & (df["Senior Management"])])












print("----------------------------------- .isin()  Method ---------------------------------")
m1 = df["Team"] == "Legal"
m2= df["Team"] == "Sales"
m3 = df["Team"] == "Product"

print(df[m1 | m2 | m3])

# or using method
df["Team"].isin(["Legal", "Sales", "Product"])

df[df["Team"].isin(["Legal", "Sales", "Product"])]

#or 

teamm = df["Team"].isin(["Legal", "Sales", "Product"])
print(df[teamm])













print("--------------------- .isnull()  and   .notnull()  methods------------------------------")

is_null = df["Team"].isnull()
print(is_null)

print(df[is_null])


is_null = df["Team"].notnull()
print(is_null)

print(df[is_null])















print("------------ .between() methods -------------------------")

betWeen = df["Salary"].between(60000, 70000)
print(betWeen)

print(df[betWeen])











print("------------ .sort_values() methods -------------------------")
df.sort_values("First Name", inplace = True)
print(df.head(5))









 


print("------------ .duplicated() methods -------------------------")

df[df["First Name"].duplicated(keep = "last")].head(5)

df[df["First Name"].duplicated(keep = "first")].head(5)

df[~df["First Name"].duplicated(keep = False)]     # just print unique values who has no duplicate value














print("------------ .drop_duplicates() methods -------------------------")

print(df.drop_duplicates()) # just drop if all column's are same on more than one rows


df.drop_duplicates(subset = ["First Name"], keep = "first")  # keep first value from duplicate elements on "First Row" columns

df.drop_duplicates(subset = ["First Name"], keep = "last")    # keep last value from duplicate elements on "First Row" columns



df.drop_duplicates(subset = ["First Name"], keep = False)  # print just unique value


print(df.drop_duplicates(subset = ["First Name", "Team"], inplace = True))  # remove if duplicate happend on both of columns
print(df.head(5))










print("------------ .unique() and nunique() methods -------------------------")
df["Team"].unique()  # total type of unique value
print(len(df["Team"].unique()))   # total number of unique items

df["Team"].nunique()  # defaultly count unique value without nan

#nunique drop nan value defaultly but if we want to count nan we need to pass false
df["Team"].nunique(dropna = False)


















