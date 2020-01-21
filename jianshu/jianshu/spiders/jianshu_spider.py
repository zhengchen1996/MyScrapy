# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JianshuSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get().replace("*", "")
        origin_url = response.url
        article_id = origin_url.split("?")[0].split("/")[-1]
        content = response.xpath("//div[@class=show-content]").get()
        word_count = response.xpath("//span[@class='wordage']/text()").get()
        comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        like_count = response.xpath("//span[@class='likes-count']/text()").get()
        read_count = response.xpath("//span[@class='views-count']/text()").get()
        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())
        item = ArticleItem(
            title=title,
            article_id=article_id,
            avatar=avatar,
            author=author,
            pub_time=pub_time,
            origin_url=origin_url,
            content=content,
            subjects=subjects,
            word_count=word_count,
            comment_count=comment_count,
            read_count=read_count,
            like_count=like_count
        )
        yield item