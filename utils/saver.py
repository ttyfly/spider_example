import json, os
from datetime import datetime, time
from settings import SAVE_PATH

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

def save(data: dict) -> str:
    # 从 data 中获取相关参数，生成文件名
    # 这里使用了 python datetime，请查阅 python 官方文档，了解这些函数的用法
    filename = data['name'] + '-' + datetime.fromisoformat(data['generated_at']).strftime('%Y-%m-%d-%H-%M-%S') + '.json'

    # 拼接出文件路径
    # 请百度了解「绝对路径」和「相对路径」的区别，以及路径中「.」和「..」的含义
    filepath = os.path.join(SAVE_PATH, filename)

    # 打开文件，并保存 json 信息
    # 请百度了解 python 文件操作的方法
    # 这里使用了 python json，请查阅 python 官方文档，了解相关函数的用法
    # 另外，这里为啥要来一个 encoding='utf-8' 呢？请百度了解 utf-8 是什么。还可以尝试删掉这个参数，看看输出结果
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    # 返回保存的文件路径，以备它用
    return filepath

    

    
    
