import pandas as pd

df=pd.read_csv("GBvideos.csv")

#1 ilk 50 kaydı getir

# result=df.head(50)
# print(result)

#2 5-10 kaydı getir

# result=df[5:10]
# print(result)

#3 Datasette bulunan kolon isimleri ve sayıları

# print(df.columns)
# print(len(df.columns))

#4 Bazı kolonları silin ve kalan kolonları listeleyin
df=df.drop(["thumbnail_link","comments_disabled","video_error_or_removed","description"], axis=1)
# result=df
# print(df)

#5- Begenme like ve begenmeme dislike ort bulunuz
# like=df['likes'].mean()
# print(like)

# dslike=df["dislikes"].mean()
# print(dslike)

#6- ilk 50 videonun like ve dislike kolonlarını getir

# result=df.head(50)[["likes","dislikes"]]
# print(result)

#7 En cok goruntulenen video hangisidir

# result=df[df["views"]==df["views"].max()][["title","views"]]
# print(result)

#8 En düşük görüntülenen video hangisidir

# result=df[df["views"]==df["views"].min()][["title","views"]]
# print(result)

#9- En fazla görüntülenen ilk 10 video

# result=df[["title","views"]].sort_values("views").head(10)
# print(result)
# result=df.iloc[5153]
# print(result)