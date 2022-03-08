import matplotlib.pyplot as plt

# yil=[2011,2012,2013,2014,2015]

# oyuncu1=[8,10,12,7,9]
# oyuncu2=[7,12,5,15,21]
# oyuncu3=[18,20,22,25,19]
"""
#stack plot

plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.title("Yıllara göre atılan goller")
plt.xlabel("yıllar")
plt.ylabel("goller")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.legend()
plt.show()
"""
"""
#Pie graphs

goal_types="Penaltı","Kaleye atılan sut","Serbest vurus"

goals=[12,35,7]

colors=["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.1,0.1,0.1),autopct="%1.1f%%")
plt.show()
"""
"""
#Bar Graphs

plt.bar([1,3,2,5,2.5],[50,40,20,30,70],label="BMW",width=.5)
plt.bar([0.7,2.24,4,3.2,1.7],[80,20,30,45,50],label="Audi",width=.5)

plt.legend()

plt.xlabel("Gün")
plt.ylabel("km")
plt.title("Arac bilgileri")
plt.show()
"""


"""
#Histogram Graphs

yaslar=[12,34,12,65,87,1,7,32,14,10,45,34,52,23,36,27,3]
yas_gruplari=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yas grupları")
plt.ylabel("kisisayısı")
plt.title("histogram graph")
plt.show()
"""