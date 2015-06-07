__author__ = 'DanielLevi'

from bs4 import BeautifulSoup
import requests
import urllib

## using requests library GET HTML from site
## note that I set objects_per_page to 150 in order to ensure that ALL products would appear on same page
## -- adjust accordingly
page = requests.get\
    ("http://magtouch.com/xcart/home.php?cat=248&sort=orderby&sort_direction=0&objects_per_page=150&page=1").content

## use BeautifulSoup to parse HTML
## constructor to create a BeautifulSoup object
soup = BeautifulSoup(page)

## extract all html contained within divs that have class = image
imageBlock = soup.find_all("div", {"class": "image"})

## iterate through results, find the url associated with the image, download images to file
imageCount = 0

for link in imageBlock:

    ## find the url to product page
    url = link.find("a")["href"]

    ## get html for product page
    page2 = requests.get("http://www.magtouch.com/xcart/" + url).content

    ## instantiate BeautifulSoup object
    soup = BeautifulSoup(page2)

    ## store image url and product number
    imageBlock = soup.find("img", {"id": "product_thumbnail"})["src"]
    imageName = soup.find("td", {"id": "product_code"}).getText()

    ## download image and store in folder
    urllib.urlretrieve(imageBlock, "/Users/DanielLevi/Desktop/Tapestries/%s.JPG" % imageName)

    ## increment imageCount
    imageCount += 1

print "You have successfully downloaded %d images!" % imageCount

