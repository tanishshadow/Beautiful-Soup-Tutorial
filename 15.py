# parent element in soup

from bs4 import BeautifulSoup as bs

html = """<html><head><title>Tutorials Point</title></head>
<body>
<p class="title"><b>The Biggest Online Tutorials Library, It's all Free</b></p>
<p class="prog">Top 5 most used Programming Languages are:
<a href="https://www.tutorialspoint.com/java/java_overview.htm" class="prog" id="link1">Java</a>,
<a href="https://www.tutorialspoint.com/cprogramming/index.htm" class="prog" id="link2">C</a>,
<a href="https://www.tutorialspoint.com/python/index.htm" class="prog" id="link3">Python</a>,
<a href="https://www.tutorialspoint.com/javascript/javascript_overview.htm" class="prog" id="link4">JavaScript</a> and
<a href="https://www.tutorialspoint.com/ruby/index.htm" class="prog" id="link5">C</a>;
as per online survey.</p>
<p class="prog">Programming Languages</p>
"""

soup = bs(html, 'html.parser')
tag = soup.title
print(tag)
print(tag.parent)  # .parent gives us the parent tag
print(tag.parent.name)  # gives the name of the parent

html_tag = soup.html
# the parent of html_TAg is the bs4 object itself----
print(type(html_tag.parent))  # <class 'bs4.BeautifulSoup'>


# the parent of beautiful soup object is none
print(soup.parent)

# iterating over the parents

for parent in soup.a.parents:
    if parent is not None:
        print(parent.name)
    else:
        print(parent)
