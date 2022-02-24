"""
1-100 arasında rasgele üretilecek bir sayıyı asagi yukarı ifadeleri ile buldurmaya calisin
** 100 üzerinden puanlama yapın her soru 20 puan
** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın


"""
import random


a=(random.randint(1,10))


print(a)


hak=5
t=0
while hak>0:
    hak=hak-1
    tahmin=int(input("tahmininiz: "))
    t=t+1
    if a==tahmin:
        print(f"tebrikler {t} defada bildiniz")
       
        break
    elif tahmin>a:
        print("asagi")
        
    elif tahmin<a:
        print("yukarı")
        
    
    if hak==0:
        print(f"hakkiniz bitmistir sayi: {a}dır")


    
    

       

   