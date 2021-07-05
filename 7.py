# about beautiful soup object 

from bs4 import BeautifulSoup as bs

soup = bs("<h2 id='message'>Hello, Tutorialspoint!</h2>","html.parser")
print(soup) 
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup.name) #document

# important points---
# BeautifulSoup is the object created when we try to scrape a web resource. So, it is the complete document which we are trying to scrape. Most of the time, it is treated like a  tag object.
