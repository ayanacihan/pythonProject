#Spiders are classes that Scrapy uses to scrape information from a website.
import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = [
        'https: // bluelimelearning.github.io / my - fav - quotes /'
    ]

    def parse(self, response): #self the instance of the class. By using this we can reach the attributes of the class we defined.
        for quote in response.css('div.quotes'):
            yield {
                'quote':quote.css('p.aquote::text').extract(),
                'author':quote.css('p.author::text').extract_first(),
            }#yield is the keyword to return. #generators are iterators.