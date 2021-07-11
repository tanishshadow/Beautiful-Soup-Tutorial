# siblings in beautifulsoup

from bs4 import BeautifulSoup as bs

html_Doc = "<a><b>TutorialsPoint</b><c><strong>The Biggest Online Tutorials Library, It's all Free</strong></b></a>"

soup = bs(html_Doc, 'html.parser')
print(soup.prettify())

# using .next_sibling and .previous_sibling

print(soup.b.next_sibling)  # gives the sibling next to b tag
print(soup.b.next_sibling.name)
print(soup.c.previous_sibling)
print(soup.c.previous_sibling.name)

#  the sibling of a string is none

print(soup.b.string.next_sibling)

#  the unexpected sibling---
html_doc2 = """ <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>"""

# here the next sibling of the first a tag may seem to be the second a tag while it's not!!! the next sibling is "\n"
print('\n\n\n')
soup2 = bs(html_doc2, 'html.parser')
print(soup2.prettify())
print('\n', repr(soup2.a.next_sibling))
#  the second a tag is actually the next sibling of the \n
print(soup2.a.next_sibling.next_sibling)
