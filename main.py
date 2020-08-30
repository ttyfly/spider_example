from spider import Spider
from spiders.wdyw import spider as wdyw_spider

# 这是程序入口
# 任务还要求实现控制台交互程序，因为比较简单，这里我就不实现了

# 创建 Spider 对象
spider = Spider()

# 注册武大要闻爬虫，当然你可以实现新的爬虫，一同注册到这个 spider 对象上
spider.register('武大要闻', wdyw_spider)

# 使能所有注册的爬虫
spider.enable_all()

# 开始爬取，并且设置按照 date 逆序排序
spider.craw(order='date', reverse=True)