#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
type = sys.getfilesystemencoding()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
html = requests.get('https://chaoshi.detail.tmall.com/item.htm?spm=a3204.7933263.0.0.ORKfkJ&id=530738505675&rewcatid=50514008',headers=headers)
# print html.text
html.encoding = 'unicode'
chinese = re.findall(u"([\u4e00-\u9fa5]+)" , html.text , re.S)
for x in chinese:
    print x



# source = "s2f程序员杂志一2d3程序员杂志二2d3程序员杂志三2d3程序员杂志四2d3"
# temp = source.decode('utf8')
# xx=u"([\u4e00-\u9fa5]+)"
# pattern = re.compile(xx)
# results =  pattern.findall(temp)
# for result in results :
#   print result


