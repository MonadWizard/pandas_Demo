import pandas as pd

# List

pd.Series()


ice_cream= ["chocolate", "vanila", "strawbarry", "Run Raisin"]
s = pd.Series(ice_cream)
print(s)

lottery= [4,115,23,42]
s1 = pd.Series(lottery)
print(s1)

registration= [True, False, True, False]
s2 = pd.Series(registration)
print(s2)

# Dictionary

webster = {"Aardvark" : "An animal", "Banana" : "A delicious fruit", "Cyan" : "A color", "Nothing" : "None"}
s3 = pd.Series(webster)
print(s3)


print("-----------------------work with attribute----------------\n\n\n")
print(s.values)

print(s.index)
print(s3.index)

print(s1.dtype)
print(s3.dtype)




print("-----------------------work with methods----------------\n\n\n")

print(s1.sum())

print(s.sum())

print(s1.product())  # multiply eatch other

print(s1.mean())

print(s1.min(), "\t", s1.max())




print("-----------------------work with Parameter AND Arguments----------------\n\n\n")

s4 = pd.Series(ice_cream,lottery)
s5 = pd.Series(data= lottery, index = registration)
s6 = pd.Series(index = webster, data = registration) 
print(s4, "\n\n", s5, "\n\n", s6)








