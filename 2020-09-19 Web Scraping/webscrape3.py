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

fav_quotes = page_soup.findAll("p", {"class":"aquote"})  #class is attribute and aquotes is parameter
fav_author = page_soup.findAll("p", {"class":"author"})  #class is attribute and author is parameter

print(fav_quotes[2])
print(fav_author[2])

#For exporting the results of the scripts, [python3 web_scraping.py > output1.txt]
