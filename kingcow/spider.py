from .request import *
import urllib
import time
import threading
class Spider():
    """
    Spider爬虫类
    用于爬取数据
    
    """
    def __init__(self,web_link,step=0,**kwargs):
        self.kwargs = kwargs
        self.step = step
        if isinstance(web_link,(list,tuple)):
            self.web_link = web_link
        if isinstance(web_link,str):
            self.web_link = [web_link]
        self.data = {}
    def request(self):
        """
        爬取网页
        """
        for i in range(0,len(self.web_link)):
            try:
                self.data[self.web_link[i]] = Request(self.web_link[i],**self.kwargs)
            except:
                continue
            time.sleep(self.step)
        Success_rate = len(self.data)/len(self.web_link)
        return 'Success rate is {}'.format(str(Success_rate))
    def Data_cleaning(self,list1):
        if not list1:
            return list1
        for i in range(0,len(list1)):
            if not list1[i]:
                del list1[i]
        return list1
    def html_data(self,tag,attrs=[],clean=True,code='utf-8'):
        """
        网页数据解析
        """
        if isinstance(code,str):
            code = [code for i in range(0,len(self.data))]        
        l = {}
        k = 0
        for i in list(self.data.keys()):
            p = self.data[i].html_analysis(tag,attrs=attrs,code=code[k])
            if clean:
                p = self.Data_cleaning(p)
            l[i] = p
            k = k+1
        return l
    def html_tag(self,tag,attrs,code='utf-8'):
        """
        网页标签解析
        """
        if isinstance(code,str):
            code = [code for i in range(0,len(self.data))]        
        l = {}
        k = 0
        for i in list(self.data.keys()):
            p = self.data[i].html_tag(tag,attrs,code=code[k])
            l[i] = p
            k = k+1
        return l
    def xml_data(self,tag,clean=True,code='utf-8'):
        """
        xml解析
        """
        if isinstance(code,str):
            code = [code for i in range(0,len(self.data))]
        l = {}
        k = 0
        for i in list(self.data.keys()):
            p = self.data[i].xml_data(tag,code=code[i])
            if clean:
                p = self.Data_cleaning(p)
            l[i] = p
            k = k+1
        return l
    def json_get(self,name,code='utf-8'):
        """
        返回爬取的json各项
        不存在返回None
        """
        if isinstance(code,str):
            code = [code for i in range(0,len(self.data))]
        l = []
        k = 0
        for i in list(self.data.keys()):
            p = self.data[i].json(code=code[i]).get(name)
            l[i] = p
            k = k+1
        return p
    def json(self,code='utf-8'):
        """
        返回爬取的json
        """
        if isinstance(code,str):
            code = [code for i in range(0,len(self.data))]
        l = {}
        k = 0
        for i in list(self.data.keys()):
            p = self.data[i].json(code=code[i])
            l[i] = p
            k = k+1
        return p        
class Spider_For_Threading(Spider):
    """
    爬虫类多线程版
    速度相比不用多线程的四分之一
    继承自Spider
    """
    def __req(self,link):
        try:
            p = Request(link,**self.kwargs)
            self.data[link] = p
        except:
            pass
    def request(self):
        """
        爬取网站
        """
        thread = []
        f = range(len(self.web_link))
        for i in f:
            t = threading.Thread(target=self.__req,args=(self.web_link[i],))
            thread.append(t)
        for i in f:
            thread[i].start()
        for i in f:
            thread[i].join()
        Success_rate = len(self.data)/len(self.web_link)
        return 'Success rate is {}'.format(str(Success_rate))
        
