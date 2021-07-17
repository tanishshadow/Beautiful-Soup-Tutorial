# kinds  of filters ---
import re
from bs4 import BeautifulSoup as bs
html = '''<html><p>Top Three</p><p><pre>Programming Languages are:</pre></p><p><b>Java, Python, Cplusplus</b></p>'''

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

soup = bs(html, 'html.parser')
soup2 = bs(html_doc, 'html.parser')

# find_all

print(soup.find_all('p'))

# regular expression ---
# gives all the tag which starts with 'p'
for tag in soup.find_all(re.compile('^p')):
    print(tag.name)

# gives all the tag which contain the letter 't'
for tag in soup.find_all(re.compile('t')):
    print(tag.name)

# list ---
for tag in soup.find_all(["a", "p"]):  # finds all the a tag or p tag in the soup
    print(tag.name)  # p p p

# true ---
for t in soup.find_all(True):  # finds all the tags in the soup
    print(t.name)
# for x in soup.find_all(True): print(x)

# functions ---


def has_class_but_no_id(tag):
    "Returns the tag which contain the class attribute in them but not the id "
    return tag.has_attr('class') and not tag.has_attr('id')


for f in soup2.find_all(has_class_but_no_id):
    print(f)
