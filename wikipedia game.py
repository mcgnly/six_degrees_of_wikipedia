__author__ = '03mcginley33'


import requests
from bs4 import BeautifulSoup

#imports all the stuff from the url
url = "http://en.wikipedia.org/wiki/Armadillo"
r = requests.get(url)
soup = BeautifulSoup(r.text)

#based on the known location of the title, saves that as the name for the wikipage object
titleLine = soup.find_all('h1', {'class':'firstHeading'})
for t in titleLine:
    #this gets fed into the wikipage object
    wikiName = t.contents[0]

#find everything in the lowest level div class that contains the links we want, makes a list
links = soup.find_all('div', {'class':'mw-content-ltr'})

#run through that list and pull out all the anchor things that will contain a link
for link in links:
    thatLink = link.find_all('a', href = True)

#for each one of those, print the text of the link that contains the beginning of the interlink url
for x in thatLink:
    if str(x.get('href')).startswith("/wiki/"):
        #this also gets fed into the wikipage object
        wikiLinks = (x['href'])


#set up the class of wikipedia pages, which will have a name and links
class WikiPage (object):
    def __init__(self, name, linksList):
        self.name = name
        self.linksList = linksList

#make one instance of the WikiPage object with the name and links from above
a = WikiPage(wikiName, wikiLinks)
print(a.name)


#make a tree
class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def insert(self, item, links = []):
        if self.value == item:
            return #do nothing
        else:
            for i in range (10):
                self.children[i]= node(item,links[])