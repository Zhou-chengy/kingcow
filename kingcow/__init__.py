"""
kingcow
一个爬虫以及网页解析库
使用示例
>>> import kingcow as kc
>>> a = kc.get('https://www.taobao.com/')#爬取淘宝网
>>> a.a.html_tag('a','href')#提取淘宝首页上的所有的链接
用户不需安装任何第三方库，方便快捷(只需依赖Python内置库)
"""
from .request import *
from .html_handle import *
from .xml_handle import *
from .api import *
from .spider import *
__all__ = ['request','html_handle','xml_handle','api','spider',
           'Request','html_pick','html_tag','Spider','Spider_For_Threading','Xml_data'
           'get','post','html_get_tag','xml_data','html_get'
]
Version = '1.0.0'
