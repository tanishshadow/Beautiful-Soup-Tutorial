# next_Siblings and previous_siblings

from bs4 import BeautifulSoup as bs
html = """
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

soup = bs(html, 'html.parser')
for sibling in soup.a.next_siblings:
    print(repr(sibling))
    print(sibling.name)


# going back and forth--

last_a_TAg = soup.find('a', id="link5")
# .next_element gives us the word which was parsed exactly after the 'a' tag
print(last_a_TAg.next_element)

# gives the previous element parsed (' and\n')
print(repr(last_a_TAg.previous_element))
