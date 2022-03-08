import pandas as pd

df=pd.read_csv("eksikveriler.csv")

print(df)

# result=df.dropna(axis=0)

# print(result)

result=df["yas"].mean()
print(result)

result=df.fillna(value=28)
print(result)