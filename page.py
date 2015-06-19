__author__ = '03mcginley33'
import requests
from bs4 import BeautifulSoup
import sys

class page (object):
    DEPTH = 3

    def __init__(self, url, parent):
        #self._name = "this is a name"
        self._url = url
        #self._depth = depth
        self._links = []
        self._parent = parent
        self._depth = 0
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
            hrefs = str(link.get('href'))

            if '/wiki/' in (hrefs)[:6]:
                self._links.append("http://en.wikipedia.org" + hrefs)
                #print (link.get('href'))
            elif 'pink' in hrefs.lower():
                print("pink found! in level %s" % (str(self._depth)))
                sys.exit()
        if self._depth < self.DEPTH:
            for lnk in self._links:
                newpage = page(lnk, self)
                newpage._depth=self._depth+1
                newpage.spider()
                #self._pages.append(newpage)
        else:

            print ("max depth reached and term not found in this branch")