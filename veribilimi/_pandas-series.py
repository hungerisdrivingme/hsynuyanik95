# from random import randint
# import pandas as pd
# import numpy as np

# numbers=[20,30,40,50]
# letters=["a","b",23,12,"hsyn"]
# pandas_series=pd.Series()
# pandas_series=pd.Series(numbers)
# pandas_series=pd.Series(letters)

# pandas_series=pd.Series(5,[1,2,3])
# pandas_series=pd.Series(numbers,["a","b","c","d"])
# dict={
#     "a":10,"b":20,"c":30,"d":50
# }

# pandas_series=pd.Series(dict)


# print(pandas_series)

# random_numbers=np.random.randint(0,50,10)

# pandas_s=pd.Series(random_numbers)
# print(random_numbers)
# print(pandas_s)

# print(pandas_s[:2])
# print(pandas_s[-2:])
# print(pandas_s[3])

# pandas_series=pd.Series([20,30,40,50],["a","b","c","d"])
# print(pandas_series)
# print(pandas_series[-1])
# print(pandas_series[['a',"c"]])

# result=pandas_series.sum()
# result=pandas_series.max()
# result=pandas_series.min()
# result=pandas_series+pandas_series
# result=np.sqrt(pandas_series)
# result= pandas_series >=30

# print(result)
# print(pandas_series[result])



import pandas as pd
import numpy as np

# opel2018=pd.Series([20,30,40,10],["astra","corsa","vectra","insignia"])
# opel2019=pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

# total=opel2018+opel2019
# print(total)
# print(total["astra"])

#************ üsttekiyle alttaki aynı sonucu verir ******************

# opel2018=pd.Series([20,30,40,10],["corsa","astra","vectra","insignia"])
# opel2019=pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

# total=opel2018+opel2019
# print(total)
# print(total["astra"])