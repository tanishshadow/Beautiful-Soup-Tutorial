# modifying the tag attribute

from bs4 import BeautifulSoup as bs
soup=bs(r"'<b id='boldest'>bold</b>'","html.parser")
tag=soup.b
tag['id']="italic" #changing the value of 'id'
print(tag)
