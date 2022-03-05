# import requests
# from bs4 import BeautifulSoup




# url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# html=requests.get(url).content

# soup=BeautifulSoup(html,"html.parser")

# list=soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=100)

# for i in list:
#     title=i.find("td",{"class":"titleColumn"}).find("a").text
#     year=i.find("td",{"class":"titleColumn"}).find("span").text
#     print(title,year)
    

