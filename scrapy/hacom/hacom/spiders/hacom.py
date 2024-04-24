import scrapy


class HacomSpider(scrapy.Spider):
    name = "hacom"
    allowed_domains = ["hacom.vn"]
    start_urls = ["https://hacom.vn/laptop-tablet-mobile"]

    #allowed_domains = ["chocolate.co.uk"]
    #start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        products = response.css("div.p-component")
        for product in products:
            # here we put the data returned into the format we want to output for our csv or json file
            p1 = product.css('div.productSummary2021 li::text').extract()
            yield{
                'id': product.attrib['data-id'],
                'name': product.css('div.p-info a::text').get(),
                'vga': p1[3].replace('\r', ''),
                'monitor': p1[4].replace('\r', ''),
                'color': p1[5].replace('\r', ''),
                'price': product.css("span::attr(data-price)").get(),
            }