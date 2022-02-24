# sehirler=["ankara","izmir"]
# n=sehirler[:] #slicing parcalama
# n[0]="malatya"
# print(sehirler)
# print(n)

def add(*params):
    return sum((params))

print(add(3,6))
print(add(3,6,12))
print(add(3,6,123,543,121))

