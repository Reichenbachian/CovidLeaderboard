from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


settings = get_project_settings()
crawler_process = CrawlerProcess(settings) 

for spider_name in crawler_process.spider_loader.list():
    spider_cls = crawler_process.spider_loader.load(spider_name) 
    crawler_process.crawl(spider_cls)
crawler_process.start()