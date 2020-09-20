from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser") #variable page_soup contains the parsed web site.
quotes = page_soup.findAll("div", {"class":"quotes"}) #this will store all the div to the class
len(quotes)
print(quotes[1])
print(quotes[1].text.strip()) #remove the brackets and returns just the text
print(page_soup.h1)
print(page_soup.h1.text.strip()) #remove the brackets and returns just the text