# girilen sayinin asal sayi olup olmadıgıbı bulunuz

sayi=int(input("sayi giriniz: "))

for a in range(2,sayi):
    if sayi%a==0:
        print("sayi asal degildir")
        break
    else:
        print("sayı asaldır")
        break



