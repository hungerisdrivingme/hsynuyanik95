from cgitb import reset
import pandas as pd
import numpy as np

data=pd.read_csv("Players.csv")
# print(data)

#1- ilk 10 kaydı getiriniz

# result=data.head(10)
# print(result)


#2 Toplam kac kayıt vardır?

# result=data.len(data.index)
#print(result)

#3 Oyuncuların ortalama boyu?

# result=data["height"].mean()
# print(result)

#4 En uzun basketcinin boyu?
# result=data["height"].max()
# print(result)

#5 En uzun bsaketcinin ismi?
# result=data[data["height"]==data["height"].max()][["Player","height"]]
#print(result)

#6- agırlıgı 80-100 arasında olan oyuncuların ismi ve oynadıkları takım

# print(data.columns)

# # result=data[(data["weight"]>=80) & (data["weight"]<=100)] [["Player","weight","collage"]]
# # print(result)

# #7 Lebron James isimli oyuncuyu bulunuz

# result=data[data["Player"] =="James"]["Player"]

# print(result)