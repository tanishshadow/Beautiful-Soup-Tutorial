# .descendants is used to iterate over all of the children and indirect children

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
soup  = bs(html_doc,'html.parser')
print(len(soup.contents)) # has only two children namely - html tag and \n
print(len(list(soup.descendants))) #33
# print(list(soup.descendants)) gives a list of all indirect and direct children

# .string
# if the tag has only one child and if its a navigable string , then the .string can be used to get that string
some_tag = soup.head.title
for i in some_tag.children:
    print(i) # Tutorials Point

print(some_tag.string) # Tutorials Point

# If a tag's only child is another tag, and that tag has a .string, then the parent tag is considered to have the same .string as its child −

parent_tag = soup.head
print(ony_Child:=parent_tag.contents[0])
print(ony_Child.string) # Tutorials Point
print(parent_tag.string)

# if the tag contains more than one thing then .string will return None

print(soup.html.string)
