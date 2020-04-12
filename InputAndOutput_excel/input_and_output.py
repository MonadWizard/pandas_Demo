import pandas as pd

# import regular updateable data from open data of newyork to take babies name using url
# just copy those url which make download csv file
URL = "https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv"
baby_name = pd.read_csv(URL)
baby_name.head()

baby_name.info()






#convert to list
l = baby_name["Child's First Name"].tolist()    # convert babies name column to python_list 

# convert to dataframe
d = baby_name["Child's First Name"].to_frame()    # convert babies name column to another single dataframe 

# convert to ", separate value"
j = ", ".join(str(baby_name) for name in baby_name["Child's First Name"])   # take too much time cause big data






# create csv file 
baby_name.to_csv("NYC Baby Name.csv",index = False)  # defaultly index=True, can be overwright csv file,and replace previous version. so we need to index=False


# insert needed columns
baby_name.to_csv("NYC Baby Name.csv",index = False, columns = ["Year of Birth", "Child's First Name", "Count"]) 

# fix encode error  if face
baby_name.to_csv("NYC Baby Name.csv",index = False, columns = ["Year of Birth", "Child's First Name", "Count"], encoding = "utf-8") 








"""                                            ...........................................................
for import xl file we need to more library
xlrd  &   openpyxl
"""

df_S = pd.read_excel("Data - Single Worksheet.xlsx")   # execute excel sheets

df_S.head()


df_M1 = pd.read_excel("Data - Multiple Worksheets.xlsx", sheetname = "Data 1")    # execute from multiple sheet to Data1
df_M1

df_M2 = pd.read_excel("Data - Multiple Worksheets.xlsx", sheetname = "Data 2")    # execute from multiple sheet to Data2
df_M2

df_M_all = pd.read_excel("Data - Multiple Worksheets.xlsx", sheetname = ["Data 1", "Data 2"])    # execute from multiple sheet , all data
df_M_all
# or
df_M_alll = pd.read_excel("Data - Multiple Worksheets.xlsx", sheetname = [0, 1])    # execute from multiple sheet , all data
type(df_M_alll)

# we can call 
df_M_all["Data 1"]

df_M_alll[0]








# export data to excel file
import pandas as pd


URL = "https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv"
baby_name = pd.read_csv(URL)
baby_name.head()
baby_name.info()


# split data to 2 excel sheet accoding to gender column.  we create boys and girls dataset to baby_name

boys = baby_name[baby_name["Gender"] == "MALE"]
girls = baby_name[baby_name["Gender"] == "FEMALE"]


# create excel file 
excel_file = pd.ExcelWriter("Baby names.xlsx")

# add data
girls.to_excel(excel_file, sheet_name = "Girls", index = False)    # import all columns with shrrt name as Girls

boys.to_excel(excel_file, sheet_name = "Boys", index = False, columns = ["Gender","Child's First Name","Count"])  # import specific columns


# now final tast create excel file and save data to it
excel_file.save()





































