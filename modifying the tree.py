from bs4 import BeautifulSoup as bs
from bs4 import NavigableString as ns
html = '<b class="bolder">Very Bold</b>'
soup = bs(html, 'html.parser')
b_Tag = soup.b
b_Tag['class'] = 'something' #this changes the soup only no changes in the original html
# print(soup)
# adding new elements

b_Tag['id'] = 0
print(soup)
# deleting the element 

del soup.b['class']
print(soup)

# modifying .string
markup = '<a href="https://www.tutorialspoint.com/index.htm">Must for every <i>Learner>/i<</a>'
Bsoup = bs(markup,'lxml')
tag = Bsoup.a
tag.string = "My Favourite spot."
print(tag)
tag.string = 'tanish'
print(tag)

Bsoup.a.append(' element') # appends into the previous string
print(Bsoup)
print(tag.contents)

# using navigable string to do the above thing -- 
soup2 = bs("<b></b>",'html.parser')
new = ns("some string")
tag = soup2.b
tag.append(new)
print(tag)


# modifying the comments -- 
from bs4 import Comment
comn = Comment("this is a comment")
tag.append(comn)
print(tag)

# adding a whole new tag -- 
print("\n\n")
new_t = soup2.new_tag("a", href="https://www.tutorialspoint.com")
soup2.b.append(new_t)
print(soup2.prettify())


