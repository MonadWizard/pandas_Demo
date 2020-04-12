import pandas as pd

salary = pd.read_csv("salary.csv", usecols = ["Age","Salary"])[["Salary","Age"]]  

print(salary)

beton = pd.read_csv("Beton.csv", usecols = ["Salary"], squeeze = True) #squeeze convert to dataframe or series
print(beton)


beton2 = pd.read_csv("Beton.csv")

print(beton2.head(),"\n\n")
print(beton2.head(10))

print(beton2.tail(),"\n\n")
print(beton2.tail(10))

print("---------------------python built in function-----------------")

print(len(beton2))   # len(series) give total number of row

print(type(beton2))

print(dir(beton2), "\n\n\n")  # see all method can be use with this data frame

sortedd = sorted(beton)
print(sortedd,"\n", type(sortedd), "\n\n\n")

print(sorted(beton2))  #sort(dataFrame) sorted data assiending orderd and create a list


print(list(beton),"\n\n\n")
print(list(beton2))          # create a list of data frame


print(dict(beton))       # create a dictionary of data frame
print(dict(beton2))

print(max(beton), "\t\t", min(beton))


print("-----------------------------more attribute---------------------")
print(beton.is_unique) # boolen compare unique value

print(beton.ndim)
print(beton2.ndim)

print(beton.shape)   # represent (row,column)
print(beton2.shape)


print(beton.size)  # total value include null
print(beton2.size)

print("-------------------------.sort_values()-----------------------")

print(beton.sort_values().head())
print(beton.sort_values(ascending = False).tail())



print("----------------------The inplace Parameter-------------------")
salary2 = pd.read_csv("salary.csv", usecols = ["Salary"], squeeze = True)
print(salary2)

print(salary2.sort_values(ascending = False, inplace = True))
print(salary2)


print("-------------------------.sort_index()-------------")

print(salary2.sort_index(ascending = False, inplace = True))
print(salary2)


print(67000.0 in salary2)
print(67000.0 in salary2.values)
print(8 in salary2)



print("------------Extravalues by Index Position-------------")
print(salary2)

print(salary2[-3:])

real = pd.read_csv("salary.csv")
print(real)


print("------------------index_col-------------")

salaryy = pd.read_csv("salary.csv", index_col = "Salary", usecols = ["Age","Salary"] , squeeze = True)
print(salaryy)


print("------------Extravalues by Index label-------------")

print(salaryy[[61000.0, 52000.0, 0.0]])

print(salaryy[61000.0 : 52000.0])




print("------------------.get() on series-------------")

print(salaryy.get(key = [61000.0, 52000.0, 0.0], default = "This is not a salary"))

print(salaryy.get(key = 0.0 , default = "This is not a salary"))



print("--------------------Math Method in series-----------------")

print(salary2.count())
print(len(salary2))
print(salary2.sum())
print(salary2.mean())
print(salary2.std())
print(salary2.min())
print(salary2.max())
print(salary2.median())  # give mid point value 
print(salary2.mode())   # represent most frequently data

print(salary2.describe())




print("-------------------- .idxmax() AND .idxmin() -----------------")

print(salaryy)

print(salaryy.max())
print(salaryy.idxmax())  #1

print(salaryy[83000.0])  #2

print(salaryy[salaryy.idxmin()])  # together 2[1]




print("-------------------- .value_counts() -----------------")

print(salaryy.value_counts())  # count repeted value +1

print(salaryy.value_counts().sum()) 
print(salaryy.count())  # same 



print("-------------------- .apply() -----------------")
print(salaryy)

def classify_performance(number):
    if number < 33:
        return "ok"
    elif number >=33 and number <=40:
        return "Satisfactory"
    else:
        return "Incredible !"


salaryy.apply(classify_performance).tail()

salaryy.apply(lambda age : age * 100)




print("-------------------- .map() -----------------")
salary3 = pd.read_csv("salary.csv", index_col = "Age", usecols = ["Age","Salary"] , squeeze = True).to_dict()

print(salary3)

print(salaryy.map(salary3))














