# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JianshuPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("pymysql",
                                            host='localhost',
                                            port=3306,
                                            user='root',
                                            passwd='zhengchen960805!',
                                            db='jianshu',
                                            use_unicode=True,
                                            charset='utf8',
                                            cursorclass=pymysql.cursors.DictCursor)
        self._sql = None

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)
        return item

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item["title"], item["content"], item["author"], item["avatar"], item["pub_time"],
                                  item["origin_url"], item["article_id"]))

    def handle_error(self, error, item, spider):
        print("="*10 + "error" + "="*10)
        print(error)
        print("="*10 + "error" + "="*10)

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article (id, title, content, author, 
            avatar, pub_time, origin_url, article_id) values (null, %s, %s, %s, %s, %s, %s, %s)"""
            return self._sql
        return self._sql