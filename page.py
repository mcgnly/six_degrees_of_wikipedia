__author__ = '03mcginley33'
import requests
from bs4 import BeautifulSoup
import sys

class page (object):
    def __init__(self, url, depth, parent):
        #self._name = "this is a name"
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
        self._name = soup.title.string
        print ("Spidering "+ self._name)

        #pulls out all the links in the wikipedia page and only displays the ones with /wiki/ in them
        for link in soup.find_all('a'):
            if '/wiki/' in str(link.get('href'))[:6]:
                self._links.append("http://en.wikipedia.org" + str(link.get('href')))
                #print (link.get('href'))
            elif 'pink' in (str(link.get('href'))).lower():
                print("pink found! in %s level" % (str(self._depth)))
                sys.exit()
        if self._depth > 0:
            for lnk in self._links:
                newpage = page(lnk, self._depth - 1, self)
                newpage.spider()
                #self._pages.append(newpage)
        else:

            print ("max depth reached and term not found in this branch")