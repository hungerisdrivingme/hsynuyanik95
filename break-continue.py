# name="Huseyin Uyanik"

# for letter in name:
#     if letter=="u":
#         continue
#     print(letter)


# x=0

# while x<5:
#     x=x+1
#     if x==3:
#         continue 
#     print(x)
    

#1-100 tek sayilarin toplami
toplam=0
x=0
while x<=100:
    x=x+1
    if x%2==0:
        continue
    
    toplam=toplam+x
print(toplam)