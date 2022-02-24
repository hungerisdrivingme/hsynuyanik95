# num=[]
# for x in range(10):
#     num.append(x)
# print(num)

# numbers=[x for x in range(10)]
# print(numbers)

# num=[]
# for x in range(10):
#     num.append(x**2)
# print(num)

# numbers=[x**2 for x in range(10)]
# print(numbers)

# number=[x*x for x in range(10) if x%2==0]
# print(number)


# mylist=[]
# mystring="hello"
# for letter in mystring:
#     mylist.append(letter)

# print(mylist)

mystring="hello"
mylist=[letter for letter in mystring]
print(mylist)

years=[1938, 1892, 1923, 1881, 1995]
ages=[2022-year for year in years]
print(ages)

numbers=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)