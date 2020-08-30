from utils.saver import save
from datetime import datetime

# 这里将要获取的数据定义为一个类
# 请百度了解什么是「面向对象」，以及「类」和「对象」的区别
# 这样的好处是什么？请百度了解什么是「基础类型偏执」，以及什么时候该用基础类型，什么时候该定义类
# 了解以上知识后，请修改你的代码，使它不再有「基础类型偏执」
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

    ## 直接调用 saver，将对象信息保存为 json
    def save(self):
        save(self.__dict__)
    
    ## 排序函数，请百度了解 python list 的 sort 方法，以及什么是「字典序」
    def sort(self, order: str, reverse: bool=False):
        self.order = order + (' reversed' if reverse else '')
        def takeItem(data):
            return data[order]
        self.data.sort(key=takeItem, reverse=reverse)