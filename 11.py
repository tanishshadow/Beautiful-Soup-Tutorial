# navigating the document using tag names
from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>Tutorials Point</title></head>
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

soup = bs(html_doc,"html.parser")
# The tag 'head'
tag_head = soup.head
print(tag_head)  # <head><title>Tutorials Point</title></head>

# The tag 'title'
tag_title = soup.title
print(tag_title)  # <title>Tutorials Point</title>

# TODO To get the first tag in the body (here the tag 'a')
tag_a = soup.body.a
print(tag_a)

# to get the first <a> tag 
tag_a_2 = soup.a
print(tag_a_2)

# to get all the tag attributes find_all is used
all_a = soup.find_all('a')
print(all_a) #gives a list
for a in all_a:
    print(a)

