# children in beautiful soup

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

soup = bs(html_doc, "html.parser")
h_tag = soup.head
print(h_tag, "<--h tag")
print(h_tag.contents, "<-- all children of head")  # contents gives the list of  all children

children = h_tag.contents
print(children[0], "<--first child")  # the first child
child_1 = children[0]
print(child_1.contents, "<--children of 1 st child")  # the children of <title>

# children of soup object 

s_con = soup.contents
# print(s_con) # the whole document
print(soup.contents[1].name,"<--1 st child of the soup")  # html

# a string can't have any children
text = soup.body.p.string
print(text.contents)  # 'NavigableString' object has no attribute 'contents'
