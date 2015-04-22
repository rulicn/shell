# -*- coding:utf-8 -*-
# author: biezhi

import urllib2
import urllib
import re
import thread
import time


#----------- 加载处理糗事百科 -----------
class QSBK:

    def __init__(self):
        self.page = 1
        self.datas = []
        self.enable = False

    # 将所有的段子都扣出来，添加到列表中并且返回列表
    def GetPage(self):
        myUrl = "http://m.qiushibaike.com/hot/page/{0}".format(self.page)
        headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

        req = urllib2.Request(myUrl, headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()

        #encode的作用是将unicode编码转换成其他编码的字符串
        #decode的作用是将其他编码的字符串转换成unicode编码
        unicodePage = myPage.decode("utf-8")

        # 找出所有class="content"的div标记
        #re.S是任意匹配模式，也就是.可以匹配换行符
        myItems = re.findall('<div.*?class="content".*?>(.*?)</div>',unicodePage,re.S)

        items = []
        for item in myItems:
            items.append([item.replace("\n","")])
        return items

    # 用于加载新的段子
    def LoadPage(self):
        # 如果用户未输入quit则一直运行
        while self.enable:
           try:
                # 获取新的页面中的段子们
                myPage = self.GetPage()
                self.datas.append(myPage)
           except:
                print '无法链接糗事百科！'

    def ShowPage(self, items):
        pos_i = 1
        # print "items={0}".format(items)
        for item in items:

            print u'第{0}页 第{1}条 {2}'.format(self.page , pos_i, item[0])
            pos_i+=1


        myInput = raw_input()
        if myInput == "quit":
            self.enable = False

    def run(self):
        self.enable = True
        page = self.page

        print u'正在加载中请稍候......'

        # 新建一个线程在后台加载段子并存储
        thread.start_new_thread(self.LoadPage,())

        #----------- 加载处理糗事百科 -----------
        while self.enable:
            # 如果self的page数组中存有元素
            if self.datas:
                items = self.datas[0]
                del self.datas[0]
                self.ShowPage(items)
                self.page += 1


#----------- 程序的入口处 -----------
print u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.1
   作者：biezhi
   日期：2015-04-22
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
"""


print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
qs = QSBK()
qs.run()
