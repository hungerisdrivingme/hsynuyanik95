import re
#regular expression

str="Python kursu: Python programlama rehberiniz"

#re.findall()

# result=re.findall("python",str)

# print(result)

# #re.split()

# result=re.split(" ",str)
# print(result)

#re.sub()

# result=re.sub(" ","-",str)
# print(result)


#re.search()

result=re.search("a",str)
result=result.span()

print(result)

