# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.spiders.Spider):
    name = 'dmoz'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = [
        "http://lab.scrapyd.cn/page/1/",
        "http://lab.scrapyd.cn/page/2/"
    ]
    """
      parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 
      该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    """
    def parse(self, response):
        """ 读取网页代码
        page = response.url.split("/")[-2]
        print(page)
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('保存文件: %s' % filename)
        :param response:
        :return:
        """
        for sel in response.xpath("//*[@id='main']/div"):
            item = DmozItem()
            item['author'] = sel.xpath('span[2]/small/text()').extract()
            item['url'] = sel.xpath('span[2]/a/@href').extract()
            item['desc'] = sel.xpath('span[1]/text()').extract()
            yield item

            # author //*[@id="main"]/div[1]/span[2]/small
            # url //*[@id="main"]/div[1]/span[2]/a
            # desc //*[@id="main"]/div[1]/span[1]

