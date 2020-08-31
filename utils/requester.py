import urllib.request as urllib2
import time

# 封装请求目标网页的功能
def request(url: str) -> str:
    # url 判空
    if url is None:
        return None
    
    # 暂停 0.1 秒，以免给网站造成压力
    time.sleep(0.1)

    # 发送请求
    # 请百度了解什么是 url
    request = urllib2.Request(url)

    # 假装自己是浏览器
    # 请百度了解什么是 http header，header的作用，以及有哪些典型的 header
    request.add_header('user-agent', 'Mozilla/5.0')

    # 获取响应信息
    response = urllib2.urlopen(request)

    # 如果状态码不为200（成功），则返回空
    # 请百度了解什么是 http 状态码，以及有哪些状态码，分别代表什么意思。
    if response.getcode() != 200:
        return None
    
    # 读取返回 body 中的信息
    # 请百度了解什么是 http body
    # 这些信息实际上是 html 格式的，请学习 html 的相关知识（重要）
    return response.read()

    # 另外，可以了解下 http GET, POST, DELETE, PUT 等请求方法，及它们的使用场景
    # 还可以了解下 http 和 https 的区别