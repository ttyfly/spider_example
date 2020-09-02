from datetime import datetime, time
from utils.saver import save

# 这里将要获取的数据定义为一个类
# 请百度了解什么是「面向对象」，以及「类」和「对象」的区别
# 这样的好处是什么？请百度了解什么是「基本类型偏执」，以及什么时候该用基本类型，什么时候该定义类
# 了解以上知识后，请修改你的代码，使它不再有「基本类型偏执」
class Data:
    # 构造函数，初始化对象数据
    def __init__(self, name: str):
        self.name = name
        self.order = 'unsorted'
        self.generated_at = datetime.now().isoformat(timespec='seconds')
        self.data = []
    
    # 成员函数
    ## 向 data 添加 item，即输出文件中一条一条的数据
    def add(self, item: dict):
        self.data.append(item)

    ## 保存数据为 json 文件
    def save(self):
        # 生成文件名。这里使用了 python datetime，请查阅 python 官方文档，了解这些函数的用法
        filename = self.name + '-' + datetime.fromisoformat(self.generated_at).strftime('%Y-%m-%d-%H-%M-%S') + '.json'
        # 直接调用 saver，将对象信息保存为 json
        save(filename, self.__dict__)
    
    ## 按规定字段顺序排序 data 条目
    def sort(self, order: str, reverse: bool=False):
        self.order = order + (' reversed' if reverse else '')
        # 直接调用 python 的排序函数。请百度了解 python list 的 sort 方法，以及什么是「字典序」
        def takeItem(data):
            return data[order]
        self.data.sort(key=takeItem, reverse=reverse)