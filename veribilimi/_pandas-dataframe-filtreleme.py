# import pandas as pd
# import numpy as np

# data=np.random.randint(10,100,75)

# data=data.reshape(15,5)

# df=pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5"])

# result=df.loc[:3] #veya
# result=df.head(4)
# result=df.loc[11:14] #veya
# result=df.tail(4)
# result=df["Column1"].head(5)
# result=df[["Column1","Column2"]].head()
# result=df[["Column1","Column2"]].tail()
# result=df[5:15][["Column1","Column2"]].head()


#****** FILTRELEME*********
# result= df>50
# print(result)
# print(df[result])

# result=df[df["Column1"]>50][["Column1","Column2"]]
# result=df[(df["Column1"]>50) & (df["Column2"]<70)]
# result=df[(df["Column1"]>50) | (df["Column2"]<70)]

# result=df.query("Column1>=50 & Column1%2== 0")
# print(result)
