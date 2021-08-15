import xml.sax
class Xml_data(xml.sax.ContentHandler):
    def __init__(self):
        self.pick_tag = []
        self.pick_data = {}
        self.m = ""
    def pick_tags(self,tag):
        self.m = ""
        if isinstance(tag,str):
            self.pick_tag = [tag]
        if isinstance(tag,(list,tuple)):
            self.pick_tag = tag
        for i in range(0,len(self.pick_tag)):
            self.pick_data[self.pick_tag[i]] = []
    def startElement(self, tag, attributes):
        if tag in self.pick_tag:
            self.m = tag
        else:
            pass
    def characters(self, content):
        if self.m:
            self.pick_data[self.m].append(content)
            self.m = ""
    
def xml_data(xmlString,tags):
    xml_parser =  Xml_data()
    xml_parser.pick_tags(tags)
    xs = xml.sax.parseString(xmlString,xml_parser)
    return xml_parser.pick_data
    
