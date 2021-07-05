# navigable string objects

from bs4 import BeautifulSoup as bs

soup = bs("<h2 id='message'>Hello, Tanish op!</h2>","html.parser")
content = soup.string
print(content)
print(type(content))  # <class 'bs4.element.NavigableString'>
 

# important points ---- The navigable string object is used to represent the contents of a tag. here for eg- "Hello, Tanish op!" To access the contents, ".string" is used with the tags.
