import pandas as pd
chicago = pd.read_csv("chicago.csv").dropna(how = "all")
# reduse memory size
chicago["Department"] = chicago["Department"].astype("category")
chicago["Position Title"] = chicago["Position Title"].astype("category")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].astype("category")

print(chicago.info())


#chicago["Employee Annual Salary"].nunique() # less unique value reduse more memory

print('------------------- .str.lower(), .str.upper(), .str.title(), .str.len()------------------')

chicago["Name"] = chicago["Name"].str.title()
chicago["Department"] = chicago["Department"].str.lower()
# count total character par row by 
chicago["Position Title"].str.len()

#count total String
print(len(chicago["Position Title"]))






print('------------------- The .str.replace() ------------------')

chicago["Department"] = chicago["Department"].str.replace("mgmnt","management")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].str.replace("$","").astype(float)





print('------------------- Filtering with String Method ------------------')

import pandas as pd
chicago = pd.read_csv("chicago.csv").dropna(how = "all")
# reduse memory size
chicago["Department"] = chicago["Department"].astype("category")
chicago["Position Title"] = chicago["Position Title"].astype("category")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].astype("category")

print(chicago.info())

# if found water in any whhere in Position Title
mask = chicago["Position Title"].str.lower().str.contains("water")
chicago[mask]

# if found water in first in  Position Title
chicago[chicago["Position Title"].str.lower().str.startswith("water")]

# if found ist in last in  Position Title
chicago[chicago["Position Title"].str.lower().str.endswith("ist")]









print('------------------- .strip(), .lstrip(), .rstrip() for remove freeSpace------------------')

import pandas as pd
chicago = pd.read_csv("chicago.csv").dropna(how = "all")
# reduse memory size
chicago["Department"] = chicago["Department"].astype("category")
chicago["Position Title"] = chicago["Position Title"].astype("category")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].astype("category")

print(chicago.info())

# remove white space from left and from right
chicago["Name"] = chicago["Name"].str.rstrip().str.lstrip()

chicago["Position Title"] = chicago["Position Title"].str.strip()









print('------------------- String Method on Index and Columns ------------------')  # problem
#print(chicago.index)

#chicago.index = chicago.index.srt.strip().srt.title()




print('------------------- Split Strings By Characters with .str.split() method ------------------')

import pandas as pd
chicago = pd.read_csv("chicago.csv").dropna(how = "all")
# reduse memory size
chicago["Department"] = chicago["Department"].astype("category")
chicago["Position Title"] = chicago["Position Title"].astype("category")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].astype("category")
chicago.head(3)

firstName = chicago["Name"].str.split(",").str.get(0).str.title().value_counts()
 
#position = chicago["Position Title"].srt.split(" ").str.get(0).value_counts()  #what the problem?





print('------------------- more Practice with Split method ------------------')



# DO


print('------------------- The expend and n Parameters of the str.split() method ------------------')

# DO