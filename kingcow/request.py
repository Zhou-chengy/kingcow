import urllib
from html.parser import *
import urllib.request
from . import html_handle
import copy
import json
from . import xml_handle
class Request():
    """
    网页请求类
    >>> import kingcow
    >>> a = kingcow.Request('https://www.taobao.com/')
    >>> a.html_tag('a','href')#提取淘宝首页上的所有的链接
    """
    def __init__(self,
                 url,
                 data=None,
                 json=None,
                 headers={},
                 ip = None,
                 origin_req_host=None,
                 unverifiable=False,
                 method=None,
                 code='utf-8',
                 *,
                 cafile=None,
                 capath=None,
                 cadefault=False,
                 context=None):
        """
        ----
        主要参数说明
        url:str类型，为网页地址
        data:请求数据，网页指定提交类型为application/x-www-form-urlencoded
        json:请求类型，网页指定提交类型为application/json
        headers:请求头
        method:模式，如GET,POST
        code:如果有data参数，会将data参数加密成code编码
        ip:使用代理ip
        """
        if json:
            data = json.dumps(json)
        if data:
            data = urllib.parse.urlencode(data).encode(code)            
        req = urllib.request.Request(url,data=data,headers=headers,origin_req_host=origin_req_host,unverifiable=unverifiable,method=method)
        if ip:
            opener  = urllib.request.build_opener(urllib.request.ProxyHandler(ip))
            self.HTTP = opener.open(req)
        if not ip:
            self.HTTP = urllib.request.urlopen(req,cafile=cafile,capath=capath,cadefault=cadefault,context=context)
        self.text = self.HTTP.read()
    def read(self,code=None):
        """
        读取网页
        """
        if not code:
            return self.text
        if code:
            return self.text.decode(code)
    def info(self):
        return self.HTTP.info()

    def geturl(self):
        return self.HTTP.geturl()
    
    def html_analysis(self,lab,attrs=[],code='utf-8'):
        """
        网页解析数据
        """
        return html_handle.html_get(self.read(code),lab,attrs)
    def html_tag(self,tag,attrs,code='utf-8'):
        """
        提取标签
        """
        return html_handle.html_get_tag(self.read(code),tag,attrs)
    def xml_data(self,tag,code='utf-8'):
        """
        xml数据解析
        """
        return xml_handle.xml_data(self.read(code=code),tag)
    def json(self,code='utf-8'):
        return json.loads(self.read(code))
