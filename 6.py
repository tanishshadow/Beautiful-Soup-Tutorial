# attribute containing more than one value but is not multi valued attribute
from bs4 import BeautifulSoup as bs

soup = bs('<p id="body bold"></p>','html.parser')
tag = soup.p
print(tag['id'])
print(type(tag['id'])) # < str >

# changing the value of the attributes

rel_soup = bs("<p> tutorialspoint Main <a rel='Index'> Page</a></p>","html.parser")
tag = rel_soup.a
print(tag)
tag['rel'] = ['Not',' something','important' ,'here'] #changing the rel (note this will be converted to a multi valued attribute [str like])

print(tag)
