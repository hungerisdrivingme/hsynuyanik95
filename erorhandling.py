
# try:    
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("y icin 0 girilemez")
# except ValueError:
#     print("tamsayı harici deger girilemez")



# try:    
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as a:
#     print("Yanlış deger girdiniz")
#     print(a)


from logging import exception


while True:
    try:
        x=int(input("x: "))
        y=int(input("y: "))
        print(x/y)
    except Exception as ex :
        print("yanlıs bilgi girdiniz",ex)
    else:
        break