from urllib.request import urlopen as uReq #alias uReq is our selection to call this import
from bs4 import BeautifulSoup as soup #to make it easy to reference we called it soup

quotes_page = 'http://quotes.toscrape.com/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
quotes = page_soup.findAll("div", {"class":"quote"}) #this will store all the div to the class

for quote in quotes:
    fav_quote = quote.findAll("span", {"class": "text"})
    aquote = fav_quote[0].text.strip()
    fav_author = quote.findAll("small", {"class": "author"})
    author = fav_author[0].text.strip()
    print(aquote)
    print(author)