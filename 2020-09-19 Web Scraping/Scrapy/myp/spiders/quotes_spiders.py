import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://bluelimelearning.github.io/my-fav-quotes/'
    ]

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {
                'quote':quote.css('p.aquote::text').extract(),
                'author': quote.css('p.author::text').extract(),
            }
#https://scrapy.org/ website is so useful for the examples and practice.
'''>>> scrapy shell 'https://bluelimelearning.github.io/my-fav-quotes/'
>>> response.css('title') #this command gives the title of the website we scrape
>>> response.css('title::text').extract() #this gives only the text part of the title
>>> quote = response.css("div.quotes")[0]
>>> aquote = quote.css("p.aquote::text").extract()
>>> aquote
'''

