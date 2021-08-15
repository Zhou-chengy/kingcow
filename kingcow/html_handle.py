from html.parser import HTMLParser
class html_pick(HTMLParser):
    def pick_lab(self,lab,attrs=[]):
        self.re = []
        self.flag = 0
        if isinstance(lab,str):
            self.pick_lab = [lab]
        if isinstance(attrs,str):
            self.pick_attrs = [attrs]
        if isinstance(lab,(list,tuple)):
            self.pick_lab = lab
        if isinstance(attrs,(list,tuple)):
            self.pick_attrs = attrs
    def handle_starttag(self, tag, attrs):
        if tag in self.pick_lab:#目标标签
            k = 0
            for i in attrs:
                if i[1] in self.pick_attrs:
                    k += 1
            if k==len(self.pick_attrs) and self.pick_attrs:
                self.flag = 1
            if not self.pick_attrs:
                self.flag = 1
                
        else:
            pass
    def handle_data(self, data):
        if self.flag==1:
            self.re.append(data.strip())
            self.flag=0
        else:
            pass
def html_get(html,lab,attrs=[]):
    pick = html_pick()
    pick.pick_lab(lab,attrs=attrs)
    pick.feed(html)    
    return pick.re
    
class html_tag(HTMLParser):
    def pick_tag(self,tag,attrs):
        self.attrs = {}
        if isinstance(attrs,str):
            self.pick_attrs = [attrs]
        if isinstance(attrs,(list,tuple)):
            self.pick_attrs = [attrs]
        if isinstance(tag,str):
            self.pick_tag = [tag]
        if isinstance(tag,(list,tuple)):
            self.pick_tag = tag
        for i in self.pick_attrs:
            self.attrs[i] = []
    def handle_starttag(self,tag,attrs):
        if tag in self.pick_tag and attrs:
            for i in attrs:
                if i[0] in self.pick_attrs:
                    self.attrs[i[0]].append(i[1])
        else:
            pass
def html_get_tag(html,tag,attrs):
    pick = html_tag()
    pick.pick_tag(tag,attrs)
    pick.feed(html)
    return pick.attrs
