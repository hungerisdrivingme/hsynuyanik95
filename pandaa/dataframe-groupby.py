import pandas as pd


personeller={
    "Çalışan":["Ahmet Yılmaz","Can Ertürk ","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman":["IK","Bilgi","Muhasebe","IK","Bilgi","Muhasebe","Bilgi"],
    "Yas":[30,25,45,50,23,34,42],
    "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Kadıköy","Tuzla","Kadıköy"],
    "Maas":[5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups

# semtler=df.groupby("Semt")
# for name,group in semtler:
#     print(name)
#     print(group)

result=df.groupby("Semt").get_group("Kadıköy")

result=df.groupby("Departman").mean()
result=df.groupby("Departman")["Maas"].mean()
result=df.groupby("Semt")[["Maas","Yas"]].mean()
result=df.groupby("Semt")["Çalışan"].count()
result=df.groupby("Semt")["Çalışan"].max()

print(result)