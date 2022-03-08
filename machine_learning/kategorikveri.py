"""
Kategorik verilerin sayısal verilere çevrilme işlemi. İlk olarak Nan degerleri 
ortalama degerle degistirdik. Ardından ulke degişkenlerini tr,fr,us 
makinanın anlayacagı sekilde 2 1 0 olarak kodladık
sonra bunu arraya cevirdik
"""


# import pandas as pd
# import numpy as np
# from sklearn.impute import SimpleImputer
# df=pd.read_csv("eksikveriler.csv")

# # print(df)

# imputer=SimpleImputer(missing_values=np.nan,strategy="mean")

# yas=df.iloc[:,:].values

# imputer=imputer.fit(yas[:,1:4])
# yas[:,1:4]=imputer.transform(yas[:,1:4])
# # print(yas)

# ulke=df.iloc[:,0:1].values
# print(ulke)

# from sklearn import preprocessing

# le=preprocessing.LabelEncoder()

# ulke[:,0]=le.fit_transform(df.iloc[:,0])

# print(ulke)

# ohe=preprocessing.OneHotEncoder()
# ulke=ohe.fit_transform(ulke).toarray()
# print(ulke)