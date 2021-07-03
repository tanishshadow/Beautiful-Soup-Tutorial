#extracting the title of a website

from bs4 import BeautifulSoup as bs
import requests

url = "https://www.tutorialspoint.com/index.htm"
req=requests.get(url)
soup=bs(req.text, "html.parser")
print(soup.title) # this gives the title of the soup object
