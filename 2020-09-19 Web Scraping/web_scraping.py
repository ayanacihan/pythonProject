#Careful before scraping. Not illegal but be careful. Check terms and conditions.
#Don't scrape agressively.
#Scrapy: Open source. pip install scrapy
#Beautiful Soup
#https://bluelimelearning.github.io/my-fav-quotes/ #use this website for scraping

from urllib.request import urlopen as uReq #alias uReq is our selection to call this import
from bs4 import BeautifulSoup as soup #to make it easy to reference we called it soup

quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
quotes = page_soup.findAll("div", {"class":"quotes"}) #this will store all the div to the class

for quote in quotes:
    fav_quote = quote.findAll("p", {"class": "aquote"})
    aquote = fav_quote[0].text.strip()

    fav_authors = quote.findAll("p", {"class": "author"})
    author = fav_authors[0].text.strip()

    print(aquote)
    print(author)