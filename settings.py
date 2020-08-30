# 配置文件
# 我们总是会将一个项目的配置单独放到一个文件里，方便之后寻找、修改
# 另外，如果配置文件中有敏感信息（如密码），我们就会将配置文件加入 gitignore 中

import os

SAVE_PATH = os.path.join(os.getcwd(), 'data')   # 配置输出文件夹

# 有时，我们还可以使用环境变量进行配置，请百度了解什么是环境变量，以及它在 windows 和 linux 中的设置方法