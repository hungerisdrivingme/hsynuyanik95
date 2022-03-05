from cgitb import reset
import numpy as np


#1- (10,15,30,45,60) degerlerine sahip numpy dizisi olustur
# a=np.array([10,15,30,45,60])
# print(a)

#2-(5-15)arasındaki sayilarla numpydizi olustur
# a=np.arange(6,15)
# print(a)

#3-(50-100)arasında 5er 5er artan diziyi olustur
# a=np.arange(50,100,5)
# print(a)

#4-10 elamanlı 0lardan olusan dizi olustur.
# a=np.zeros(10)
# print(a)


#5-10 elemanlı "1"lerden olusan dizi olustur.
# a=np.ones(10)
# print(a)

#6-(0-100)arasında esit aralıklarla 5 sayı üret
# a=np.linspace(0,100,5)
# print(a)

#7-(10-30)arasında rastgele 5 tamsayı
# a=np.random.randint(10,30,5)
# print(a)

#8- [-1 ile 1] arasında 10 adet sayı üret
# a=np.random.randn(10)
# print(a)

#9- (3x5) boyutlarında (10-50)arasında rastgele matris olustur

# a=np.random.randint(10,50,15)
# print(a)
# result=a.reshape(3,5)
# print(result)


#10-üretilen matrisin satır ve sütun sayıları toplamı?
# print(np.ndim(a))


#11- üretilen matrisin max,min ve ort. degeri

# b=np.max(result)
# b=np.min(result)
# b=np.mean(result)
# print(b)

#12- üretilen matrisin en b. degerinin indeksi kactır

#13- (10-20) arasındaki sayıları iceren dizinin ilk 3 elemanı secin
a=np.arange(10,20)
# b=a[0:3]
# print(b)

#14-Üretilen dizinin elemanlarını tersten yazdırın.

print(a[::-1])

#15-Üretilen matrisin ilk satırını secin

matrs=a.reshape(5,2)
print(matrs)
print(matrs[0])

#16-üretilen matrisin 2. satır 2. sütun elemanı nedir
print(matrs[1,1])

#17- üretilen matrisin tüm satırlardaki ilk elemanı secin
print(matrs[:,0])

#18- Üretilen matrisin her bir elemanın karesini alın
print(matrs**2)

#19Üretilen matrisin elemanlarının hangisi pozitif cift  sayıdır.
#Aralıgı (-50,50) yapınız

result=matrs %2==0
print(result)
print(matrs[result])

