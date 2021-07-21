# find_all function

import re
from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = bs(html_doc, "html.parser")

# method signature -- find_all(name, attrs, recursive, string, limit, **kwargs)
# find_all method finds all the tag that matches the descendants from the soup

title_tag = soup.find_all('title')
print(title_tag)  # [<title>The Dormouse's story</title>]

p_Tag = soup.find_all('p', 'title')
print(p_Tag)  # [<p class="title"><b>The Dormouse's story</b></p>

# ^ the second argument passed here is the attribute so find_all finds all the p tag which contains the attribute title

id_tag = soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
print(id_tag)


pattern = re.compile('sister') 
sisters = soup.find_all(string=pattern) # searches a string from the document which contains the word sister
print(sisters) # ['Once upon a time there were three little sisters; and their names were\n']
