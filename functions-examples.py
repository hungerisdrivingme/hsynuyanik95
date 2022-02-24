# gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız
# def fonksyon(adet,cumle):
#     a=0
#     while a!=adet:
#         print(cumle)
#         a=a+1
# cumle= input("cumle giriniz: ")

# print(fonksyon(6,cumle))


#2 kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ceviren fonksiyonu

# def func(*params):
#     liste=[]
#     for param in params:
#         liste.append(param)
#     return liste
# result= func(10,20,30,"meraba")
# print(result)


#3 gonderilen 2 sayı arasındaki tum asal sayıları bulun

# sayi1= int(input("sayi1: "))
# sayi2= int(input("sayi2: "))

# def asal(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if (sayi%i==0):
#                     break
            
#             else:
#                 print(sayi)

# asal(sayi1,sayi2)


#4 kendisine gönderilen bir sayının tam bölenlerini bir liste seklinde döndürünüz

def dondur(sayi):
    tambolenler=[]
    for i in range(2,sayi):
        if (sayi%i==0):
            tambolenler.append(i)

    return tambolenler 

print(dondur(20))


    