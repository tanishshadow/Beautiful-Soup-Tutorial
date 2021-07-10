# .string and stripped strings

from bs4 import BeautifulSoup as bs

html =  """<html><head><title>Tutorials Point</title></head>
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
# finding all the strings 

for string in soup.strings:
    print(repr(string)) 
    


# .strings gives a generator containing all the strings
print(soup.strings)
print(soup.get_text()) #gives the string directly instead

# to remove extra whitespaces we need to use .stripped_strings

for i in soup.stripped_strings:
    print(repr(i))
