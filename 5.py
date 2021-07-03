# multi valued attributes

from bs4 import BeautifulSoup as bs

soup = bs('<p class="body"></p>',"html.parser")
tag = soup.p
print(tag['class']) # ['body']

soup2 = bs('<p class="body bold"></p>',"html.parser")
tag2 = soup2.p
print(tag2['class']) # ['body','bold]
