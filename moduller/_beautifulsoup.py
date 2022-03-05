html_doc="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilkwebsayfam</title>
</head>
<body>
    <h1>
        Python kursu
    </h1>
    <div>
        <h2>
            programlama
        </h2>
        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ul>
    </div>
</body>
</html>


"""




from bs4 import BeautifulSoup



soup=BeautifulSoup(html_doc,'html.parser') 

result=soup.prettify()
result=soup.title()

result=soup.title.string

result=soup.h1

result=soup.find_all("h2")

result=soup.div.findChildren()
print(result)


