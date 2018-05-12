# -*- coding:utf-8 -*-

import sys
from pandas import DataFrame
import pandas as pd

import xml.sax
import xml.sax.handler


#dict_data_f1 = pd.read_table("/home/zhangliang/GraduationPro/datadl/test/test.txt", sep='\t', names=["word", "type"])


'''
class xmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.text = ""
        self.infon = ""
        self.startLoc = ""
        self.endLoc = ""

    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == "passage":
            text = self.text
            rawtext = text.split(" ")
            for kv in rawtext:
                kv = kv + "\tO"
            print "rawtext:",rawtext
        elif tag == "infon":
            if infon.attributes['key'] == "MESH"
                print "wordtype:", self.infon
        elif self.CurrentData == "location":
            print "startLoc:" ,  attributes["offset"]
            print "endLoc:" , int(attributes["offset"])+int(attributes["length"])
        

    def endElement(self,tag):
        pass

    def characters(self,content):
        if self.CurrentData == "text":
            self.text = content
        elif self.CurrentData =="infon":
            self.infon = content


if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)
 
   # 重写 ContextHandler
   Handler = xmlHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("cdr.xml")        
'''

import  xml.dom.minidom

dom = xml.dom.minidom.parse('cdr.xml')
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
