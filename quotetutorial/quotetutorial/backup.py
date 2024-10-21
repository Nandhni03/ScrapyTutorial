import scrapy

from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items



# scrapy crawl quotes
# scrapy shell "http://quotes.toscrape.com/"

# response.css("span.text::text")[1].extract()
# response.css("title::text").extract_first()
# response.css(".author::text").extract()

# response.xpath("//title/text()").extract()
# response.xpath("//span[@class='text']/text()").extract()

# response.css("li.next a").xpath("@href").extract() (next page)
# response.css("a").xpath("@href").extract() (all the pages)

        # next_page = response.css('li.next > a::attr(href)').get()
        # print(next_page)
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        # next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.page_num) + '/'
        # print(next_page)
        # if QuotesSpider.page_num < 11:
        #     QuotesSpider.page_num += 1
        #     yield response.follow(next_page, callback=self.parse)
