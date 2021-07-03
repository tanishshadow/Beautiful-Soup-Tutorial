# tag object
from bs4 import BeautifulSoup as bs
soup = bs('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag.name) #name of the tag
tag.name="tanish op" #changing the tag name
print(tag.name)
print(type(tag)) #type of the tag
