from BeautifulSoup import BeautifulSoup
import urllib2

prefix = "http://en.wikipedia.org/wiki/"

lines = open('wikipedia.txt', 'r').read().split("\n")
print lines

url = prefix+lines[0]

req = urllib2.Request(url)
req.add_header('User-Agent' , 'Mozilla/5 (Solaris 10) Gecko')
r = urllib2.urlopen(req)
soup = BeautifulSoup(r)
print soup('p')

