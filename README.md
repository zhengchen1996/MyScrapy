# 此项目爬取简书网
创建爬虫
进入项目路径
scrapy startproject jianshu
cd  jianshu
scrapy genspider -t crawl jianshu_spider "jianshu.com"

导包
pypiwin32、scrapy、pymysql、Selenium

分析页面，编写爬虫
查看网页源码，如果没有想要的数据，则数据是通过ajax请求得来的，这时候就需要selenium和chromedriver来搞定

jianshu_spider.py文件中：
什么情况下使用follow：如果再爬取页面的时候，需要把满足当前条件的url再进行跟进，就设置为True，否则False，即这个url是否重新进入rules来提取url地址
什么情况下使用callback：如果这个url对应的页面，只是为了获取更多的url，并不需要里面的数据，就不需要指定callback，如果想要获取url对应页面里的数据，就要指定callback
Xpath索引是从1开始

在pipelines.py里将爬下来的数据保存到MySQL：
在navicat里创建数据库：jianshu
新建表article，并对应创建字段

开启start.py
