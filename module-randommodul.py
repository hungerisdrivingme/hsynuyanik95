import random


# val=help(random.randint)
# print(val)


# result= random.random()*100

# print(result)

result=random.randint(1,100)

print(result)

names=["ali","veli","osman","ayse"]

# a=names[random.randint(0,3)]
# print(a)


result=random.choice(names)
print(result)


liste=list(range(10))
random.shuffle(liste)
print(liste)


liste=range(100)
result=random.sample(liste,3)
print(result)

