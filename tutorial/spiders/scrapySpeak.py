import scrapy


class ScrapySpeak(scrapy.Spider):
    name = 'scrapySpeak'
    start_urls = [
        'https://segmentfault.com/a/1190000013178839',
        # 'http://www.itcast.cn/channel/teacher.shtml',
    ]

    def parse(self, response):
        filename = '123.html'
        open(filename, 'wb').write(response.body)

