# More on filters ---
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString as ns
import re

html = """
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


def not_lacie(href):
    return href and not re.compile("lacie").search(href)


# finds the tag which have href in them and uses the function above to filter in that tag
print(soup.find_all(href=not_lacie))


def surrounded_by_strings(tag):
    "Returns the tag which are surrounded by a string object"
    return isinstance(tag.next_element, ns) and isinstance(tag.previous_element, ns)


for t in soup.find_all(surrounded_by_strings):
    print(t.name)
