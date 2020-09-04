from bs4 import BeautifulSoup
from datetime import datetime
import re

from utils.requester import request
from utils.data import Data

# 这里使用了下划线命名法，请百度什么是「下划线命名法」，什么是「驼峰命名法」
base_url = 'https://news.whu.edu.cn/'
index_url = 'https://news.whu.edu.cn/wdyw.htm'

def spider() -> Data:
    # 调用 requester，获取 html 信息
    # 请先看完 utils.requester，再继续阅读
    html = request(index_url)
    if html is None:
        print('Requesting ' + index_url + ' failed.')
        return
    
    # 根据获取的 html，生成 BeautifulSoup 对象，请查阅 BeautifulSoup 官方文档，了解用法
    # 这里为啥要来一个 from_encoding='utf-8' 呢？请百度了解 utf-8 是什么
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    # 下面有关 BeautifulSoup 的部分，请对照武大要闻网站源码和 BeautifulSoup 文档阅读
    div_list = soup.find_all('div', class_='infotitle')

    # 获得 Data 对象，请先看完 utils.data，再继续阅读
    data = Data('武大要闻')  

    # 遍历获取到的全文 urls
    for url in [base_url + div.a['href'] for div in div_list if div.a is not None]:
        html = request(url)
        if html is None:
            print('Requesting ' + url + ' failed.')
            continue

        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

        title = soup.find('div', class_='news_title').string
        attrib = soup.find('div', class_='news_attrib').string
        content = soup.find('div', class_='v_news_content').get_text()

        # 为 data 添加条目
        # 这里用到了 python datetime，请查阅 python 官方文档，了解这些函数的用法
        # 这里还用到了正则表达式，请百度学习正则表达式的相关知识
        data.add({
            'title': title.strip(),
            'date': datetime.fromisoformat(
                        re.search(r'发布时间：(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})', attrib).group(1)
                    ).isoformat(timespec='seconds'),
            'from': re.search(r'来源：(\S*)', attrib).group(1),
            'content': content.strip(),
            'source_url': url
        })
    
    return data
        

    