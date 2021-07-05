# replacing the string

from bs4 import BeautifulSoup as bs

soup = bs("<h2 id='message'>Hello, Tanish op!</h2>", "html.parser")
soup.string.replace_with("LOL")
print(soup.string) #lol
print(soup)

# NOTE  we can't modify the existing string
