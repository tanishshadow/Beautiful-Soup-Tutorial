from bs4 import BeautifulSoup as bs
# printing the value of id attribute
soup=bs(r"'<b id='boldest'>bold</b>'","html.parser")
tag=soup.b
print(tag['id'])
