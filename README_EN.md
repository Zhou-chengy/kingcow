# kingcow

## This is a library for web page requests, web page parsing and crawlers

### Download

You can use two download methods, which need to be judged according to different situations

Note: the kingcow library is incompatible with Python 2

#### Pypi Download

Pypi is the python package index, and the kingcow library can be downloaded with pypi

```

python -m pip install kingcow

```

#### GitHub source code download

Copy kingcow to the site packages file in the Lib directory of the Python interpreter

### Web tag parsing

Kingcow provides the resolution of web page tags. You only need to provide the name and property of the tag, and it will return the value of the property

```Python

import kingcow as kc

a = kc.get(' https://www.taobao.com/ '# returns a kingcow. Request object and sends the request using get

print('a.html_ tag('a','href'))

```

This code will print out all the links on the home page of Taobao. You can visit other sites of Taobao according to these links

### Web page data analysis

Kingcow provides network data analysis, which can quickly and easily analyze web page data. You only need to provide tags and attributes (optional)

```Python

import kingcow as kc

a = kc.get(' https://docs.python.org/zh-cn/3.8/tutorial/index.html ')

a.html_ analysis('p')

```

The code will print out the data labeled P in the official Python document

You can also use JSON class methods to get the returned JSON

### Web crawling

Kingcow provides request methods such as request class and get and post functions. The parameters of these request methods are roughly the same, but please do not fill in method in get and post.

#### Description of main parameters

URL: STR type, which is the web page address

Data: request data. The specified submission type of the web page is application / x-www-form-urlencoded

JSON: request type. The specified submission type of the web page is application / JSON

Headers: request header

Method: mode, such as get and post

Code: if there is a data parameter, the data parameter will be encrypted into code code

IP: use proxy IP

### Spider reptile

Spider reptiles have two classes, spider and spider_ For_ Threading, let's introduce spider first

#### Spider

Spider is a crawler class that crawls multiple websites. The required parameters are roughly the same as those of the request class. The difference is that spider does not need to provide a URL. It only needs to provide a collection of URLs (not a set, but a list). It can also provide a step, which is the crawling interval.

After the spider is initialized, the website will not be crawled. Users must use the spider.request method to crawl

Spider also has four class methods (except spider. Request):

html_ Data: Web page data analysis

html_ Tag: Web page tag parsing

xml_ Data: XML data parsing

json_ Get: JSON tag item extraction

JSON: JSON extraction

#### Spider_ For_ Threading

Spider_ For_ Threading is the multithreaded version of spider, and its speed is 4 times that of spider. The specific method is the same as that of spider
