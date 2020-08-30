# spider_example

这是一个爬虫项目的示例代码。

## 运行方法

将项目 clone 到合适的地方，然后切换到项目根目录下，运行以下命令。

建立虚拟环境（可选）：

```
python -m venv venv
```

安装依赖：

```
pip install -r requirements.txt
```

运行：

```
python ./main.py
```

---

# 附：2020后台组夏令营培训计划

### 任务一（8.29-9.5）

学习 Python，编写一个简单的 Python 爬虫。

要求：


1. 学员自行决定爬取的网站，但应爬取新闻、通知、文章等周期性更新的信息。
2. 每条信息应含有如标题、更新时间、作者、内容、源地址等的4条以上的字段。
3. 时间应格式化为「年-月-日T时:分:秒」的格式（使用 Python datetime）。
4. 可以根据控制台用户输入来控制**爬取条数**和**排序标准**，将爬取结果以 JSON 格式输出到文件中（每次输出生成新文件）。
5. 文件应包含排序标准和生成时间。

另，如果爬取的内容含有图片，可以将图片保存到一个文件夹下，然后在 JSON 信息中包含图片路径，但不作严格要求，可以直接忽略图片。

**注意：**爬取速度不宜过快，内容不宜过多，防止对网站造成影响。

例子：

源网站：[武大新闻网的武大要闻](https://news.whu.edu.cn/wdyw.htm)

输出文件内容（武大要闻-2020-08-15-15-29-21.json）：

```json
{
    "name": "武大要闻",  
	"order": "date reversed",
	"generated_at": "2020-08-15T15:29:21",
	"data": [
		{
			"title": "选调生校友风采：青春与祖国共奋进",
			"date": "2020-08-14T15:12:00",
			"source": "学生就业指导与服务中心",
			"content": "......"
		},
		{
			"title": "王行环教授团队在生物医用高分子材料领域取得新进展",
			"date": "2020-08-13T20:10:00",
			"source": "第二临床学院",
			"content": "......"
		},
		{
			"title": "李斐当选南极地理信息常设委员会联合主席",
			"date": "2020-08-13T15:07:00",
			"source": "中国南极测绘研究中心",
			"content": "......"
		}
	]
}
```
**参考资料：**

**Python 学习**


1. [Python 官方文档](https://docs.python.org/zh-cn/3.7/index.html)
2. [廖雪峰的 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

**HTML/CSS 学习**


1. [w3school](https://www.w3school.com.cn/h.asp)
2. [MDN](https://developer.mozilla.org/zh-CN/docs/Web/HTML)（Mozilla 挺住）

*（不需要每个标签都看，先掌握概念，之后遇到问题时查阅即可）*

**慕课网视频**


1. [Python 开发简单爬虫](http://www.imooc.com/learn/563)
2. [Python 遇见数据采集](http://www.imooc.com/learn/712)

**爬取方法**

利用 BeautifulSoup、正则表达式或是你认为性能更好的办法。[BeautifulSoup官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)（有中文文档哦）



### 任务二（9.2-9.5）

学习 Git，注册 Github 账号。并将任务一作品上传到 Github 仓库。注意用 gitignore 忽略掉生成的 JSON 文件。在9月5日前，提交 Github 仓库地址。

**参考资料：**


1. [廖雪峰的 Git 教程](https://www.liaoxuefeng.com/wiki/896043488029600)
2. [学习 Git 分支](https://learngitbranching.js.org/)（交互式学习）

*（上传到 Github 只需要学习上面教程的很小一部分，其它部分可以日后学习）*




---


**遇到了问题？**


1. [百度](https://www.baidu.com)
2. [Bing](https://cn.bing.com)
3. [Google](https://www.google.com)

**还是没法解决？**

在群中提出问题，或者私戳学长提问也可。发送长代码可以使用[Pastebin](https://paste.ubuntu.com/)。


---





自强 Studio 技术中心后台组

2020年8月29日


