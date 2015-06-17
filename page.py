__author__ = '03mcginley33'
import requests
from bs4 import BeautifulSoup

class page (object):
    def __init__(self, url, depth, parent):
        self._name = ""
        self._url = url
        self._depth = depth
        self._links = []
        self._parent = parent
        pass

    def getName (self):
        return self._name

    def getLinks(self):
        return self._links

    def getUrl(self):
        return self._url

    def getDepth(self):
        return self._depth

    def getParent(self):
        return self._parent

    def spider(self):
        #imports all the stuff from the url
        r = requests.get(self._url)
        soup = BeautifulSoup(r.text)

        #based on the known location of the title, saves that as the name for the wikipage object
        self._name = soup.find_all('h1', {'class':'firstHeading'})

        #find everything in the lowest level div class that contains the links we want, makes a list
        links = soup.find_all('div', {'class':'mw-content-ltr'})

        #run through that list and pull out all the anchor things that will contain a link
        for link in links:
            thatLink = link.find_all('a', href = True)

        #for each one of those, print the text of the link that contains the beginning of the interlink url
        for x in thatLink:
            if str(x.get('href')).startswith("/wiki/"):
                #this also gets fed into the wikipage object
                self._links = (x['href'])

        if self._depth > 0:
            for l in self._links:
                newpage = page(self, self._depth-1, self)



    def spider(self):
        #print "Spidering"

        # beautiful soup the URL
        self._name = 'Real Name'
        linklinst = ['abc', 'cde']

        if self._depth > 0:
            for l in linklinst:
                newpage = page(l, self._depth - 1, self)
                newpage.spider()
                self._pages.append(newpage)
        else:
            pass
            #print "max depth"