# stack_overflow

运行说明：

下载项目文件；安装必要 python 库

1.命令行操作

scrapy crawl soqa（项目级命令,进入项目所在目录时使用）

2.pycharm打开项目，编缉文件调试运行配置:

点击Run->Edit Configurations,新建一个运行的python模块。

Name：改成soqa（爬虫名）； 

Script path--选择当前项目下的main.py

Parameters--crawl+要调试运行的spider名称，这里是crawl soqa

Working directory--填项目所在主目录

最后要注意点“Apply”，不要直接点“OK”

计划实现的功能：


基于用户的输入的关键词，爬取专业文档网站（Stack Overflow），
能根据用户选择来确定哪些查询结果需要存储（比如让用户勾选，选取前xx条posts等），
去掉重复的检索结果，并存成可以下一步处理的格式（csv格式）。
用户可以根据需要选取检索词，选定检索结果数量等。

