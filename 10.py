# comments

from bs4 import BeautifulSoup as bs

soup = bs('<p><!--oops comments COMMENTS  --></p>','html.parser')
print(soup.p.string)  # oops comments COMMENTS
print(soup.p.prettify()) # multi line
print(soup.p) # single line

