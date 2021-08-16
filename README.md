# kingcow

## 这是一个用于网页请求、网页解析和爬虫的库

### 下载

可以使用两种下载方式，需要根据不同的情况来判断

注意:kingcow库在Python2版本下会出现不兼容的问题

#### Pypi下载

Pypi是Python包索引，kingcow库可以用Pypi下载

```
python -m pip install kingcow
```

#### github源码下载

复制kingcow到Python解释器的Lib目录的site-packages文件下


### 网页标签解析

kingcow提供了网页标签的解析，您只需提供标签的名称与属性，他就会返回属性的值

```Python
import kingcow as kc
a = kc.get('https://www.taobao.com/') # 返回一个kingcow.Request对象，使用GET发送请求
print('a.html_tag('a','href'))
```
这段代码会打印出淘宝网首页的所有链接，你可以根据这些链接访问淘宝网的其他站点

### 网页数据解析

kingcow提供网络数据解析，可以快速方便解析网页数据，您只需提供标签和属性(可选)

```Python
import kingcow as kc
a = kc.get('https://docs.python.org/zh-cn/3.8/tutorial/index.html')
a.html_analysis('p')
```
代码会打印出Python官方文档中为标签p的数据

还可以用json类方法获取返回json

### 网页爬取

kingcow提供了Request类以及get,post函数这些请求方法，这几种请求方法的参数大致相同，但get和post中请不要填method。

#### 主要参数说明

url:str类型，为网页地址

data:请求数据，网页指定提交类型为application/x-www-form-urlencoded

json:请求类型，网页指定提交类型为application/json

headers:请求头

method:模式，如GET,POST

code:如果有data参数，会将data参数加密成code编码

ip:使用代理ip

### Spider爬虫

Spider爬虫有两个类，分别为Spider和Spider_For_Threading，我们先来介绍Spider

#### Spider

Spider是一个爬取多个网站的爬虫类，所需的参数大致与Request类相同，不同的是Spider不需要提供url，只需提供url的集合(不是set,是list)，还可以提供step，为爬取间隔。

Spider初始化后不会爬取网站，必须要用户使用Spider.request方法爬取

Spider还有四个类方法（Spider.request除外）:

html_data:网页数据解析

html_tag:网页标签解析

xml_data:xml数据解析

json_get:json标签项提取

json:json提取

#### Spider_For_Threading

Spider_For_Threading是Spider的多线程版本，速度是Spider的四分之一，具体方法同Spider

