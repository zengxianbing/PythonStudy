__author__ = 'xianbing'
# -*- coding: utf-8 -*-
import string
import urllib2
import re
import os
import sys
from string import maketrans
reload(sys)
sys.setdefaultencoding('utf-8')
def tran(str):
    intab = '<>:"/\|?*'
    outtab = "666666666"
    trantab = maketrans(intab, outtab)
    return str.translate(trantab)

def duoban_down(url,title,index):
        # sName = unicode((title.strip().replace('\t',"").replace('】',"")+ '.html'),'utf-8')#自动填充成六位的文件名
        sName = unicode((title.strip().replace('\t','').replace(':','')+ '.html'),'utf-8')#自动填充成六位的文件名
        # sName=tran(sName)


        print '正在下载第' + url + '个网页，并将其存储为' + sName + '......'
        f = open(sName,'w')
        m = urllib2.urlopen(url).read()
        f.write(m.encode('utf-8'))
        f.close()
        # os.rename(sName, '%s.html' % title)

url="http://www.douban.com/people/yeka52/notes"
s=urllib2.urlopen(url).read()

urls=re.findall(r'data-url="([^"]*)"',s,re.I)
# urls = str(urls).decode('utf8').encode('utf8')
for i in urls:
    print i
else:
    print 'this is over'

# titles=re.findall(r'data-title="([^"]*)" ',s,re.I)
titles=re.findall(r'data-title=.*? ',s,re.I)
# titles = str(titles).decode('utf8').encode('utf8')
for i in titles:
    print i[15:]
else:
    print 'this is over'
print urls
# i=1
# for index in range(len(urls)):
#
#     print
#     print urls[index],titles[index][15:]
#     url,title= urls[index],str(titles[index])[15:].decode('utf-8').encode('utf-8')
#     duoban_down(url,title,i)
#     i=i+1
# else:
#     print 'this is over'
i=0
def down_all(urlss,begin_page,end_page):
    for i in range(begin_page, end_page+10):
        s=urllib2.urlopen(urlss+str(i)).read()
        titles=re.findall(r'data-title=.*? ',s,re.I)
        urls=re.findall(r'data-url="([^"]*)"',s,re.I)
        for index in range(len(urls)):
          print urls[index],titles[index][15:]
          url,title= urls[index],str(titles[index])[15:].decode('utf-8').encode('utf-8')
          duoban_down(url,title,i)

        else:
           print 'this is over'
down_all('http://www.douban.com/people/yeka52/notes?start=',30,610)