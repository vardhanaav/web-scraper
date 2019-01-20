from bs4 import BeautifulSoup


html_doc = """
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

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.body)
#print(soup.head)
#print(soup.title)

#find() gives the first occurence
#el = soup.find('body')
#print(el)

#find_all() or findAll()
# el = soup.find_all('p')
# print(el)
# print("------------ALL[1]--------------")
# el = soup.find_all('p')
# print(el[1])

# el = soup.find(id='link1')
# el = soup.find(class_='sister')

# el = soup.find(attrs={"class":"sister"})

# select : similar to jquery
# el = soup.select('#link1')
# el = soup.select('#link') #return []
# el = soup.select('.item')[0]

# get_text: remove the html items
# el = soup.find(class_='sister').get_text() # returns Elsie

# for item in soup.select('.href'):
#     print(item.get_text())

# for item in soup.find_all('a'):
#     print(item.get_text()) # return Elsie Lacie Tillie

# el = soup.body.contents[3].contents[1].find_next_sibling()
# el = soup.body.contents[3].contents[2].find_previous_sibling()
# el = soup.body.contents[3].contents[1].find_parent()
# el = soup.find('h3').find_next_sibling('p') # search according to tag p - paragraph


print(el)
