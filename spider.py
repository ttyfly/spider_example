# 定义 Spider 类
# 什么是类？请百度了解什么是「面向对象」，以及「类」和「对象」的区别
# 这是一个管理所有 spider 的工具
# 为什么要这样做？一般编程时，我们要考虑程序的可拓展性。我们不可能满足于只爬一个网站。这样设计，就可以管理多个网站的爬虫了
class Spider:
    # 构造函数
    def __init__(self):
        self.spiders = {}
        self.enabled = []

    # 成员函数
    ## 注册爬虫
    def register(self, name: str, spider: 'function'):
        self.spiders[name] = spider
    
    ## 爬取数据
    def craw(self, order: str='unsorted', reverse: bool=False):
        for name in self.enabled:
            data = self.spiders[name]()
            if order != 'unsorted':
                data.sort(order, reverse)
            data.save()
    
    ## 使能爬虫
    def enable(self, name):
        self.enabled.append(name)

    ## 使能所有爬虫
    def enable_all(self):
        self.enabled = [name for name in self.spiders]

    ## 关闭爬虫
    def disable(self, name):
        self.enabled.remove(name)

    ## 关闭所有爬虫
    def disable_all(self):
        self.enabled = []
    
    # 为什么要设计使能？这样我们就可以安排需要爬取的网站，防止每次调用都要访问所有网站


