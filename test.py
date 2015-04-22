#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: biezhi

import urllib,urllib2,re,json,datetime,sys

#域名预定爬虫类
class DomainSearch:

    #初始化方法，定义一些变量
    def __init__(self):
        
        #查询多少条
        self.pageCount = 1
        #查询那一天的
        self.day = 1
        #反链个数
        self.rank_count=20
        #分割线
        self.div_line ="--------------------------"
        #超时设置
        self.timout=10
        # 编译好的pattern
        self.bd_pattern = re.compile(r'百度为您找到相关结果约(\d+,?)+个')
        # 查询域名数据的头信息
        self.domain_header = {
                'Origin':'http://www.22.cn',
                #'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Referer':'http://www.22.cn/YuDing/guoji/',
                'X-Requested-With':'XMLHttpRequest',
                'Connection':'keep-alive','RA-Ver':'2.9.0'}
        # 查询百度反链的头信息
        self.bd_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"}
        
    # 获取json数据
    def getJsonData(self):
        try:
            #post_url = 'http://www.22.cn/ajax/YuDing/liebiao.ashx?t=0.7920176072511822&type=en'
            post_url = 'http://121.42.158.166/data.txt'
            
            parameters = {'pageIndex':'1','pageCount': self.pageCount,'position':'1','doublep':'0','digit':'1,2,3','sskt':'1','regyear':'0','deltype':'0','suffix':'.com,.net','day':self.day,'show':'1','type':'0','strlen':'5,15'}
        
            data = urllib.urlencode(parameters)

            # request = urllib2.Request(post_url, data, headers)

            request = urllib2.Request(post_url)

            response = urllib2.urlopen(request)

            page = response.read(self.timout*1000)

            return page

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"获取数据失败,错误原因",e.reason
                return None

    # 重新加载所有数据 并计算进度
    def reLoadData(self):
        tbody = ''
        # 重新检索
        jdata = self.getJsonData().decode('utf-8')

        strdata = json.loads(jdata)

        if len(strdata['data']) > 0:
            for domainkey in strdata['data']:

                rank_num = self.searchRank(domainkey['Fulldomain'].encode('utf-8'))
                # rank_num = 100

                if rank_num > dm.rank_count:
                    tbody += '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>'\
                        .format(domainkey['Fulldomain'].encode('utf-8'), domainkey['BeianNum'].encode('utf-8'),
                                domainkey['Regdate'].encode('utf-8'), domainkey['Deldate'].encode('utf-8'), str(rank_num),
                                domainkey['BdWeight'].encode('utf-8'))

        return tbody



    # 查询百度反链
    def searchRank(self,domain):
        try:
            url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=www.' + domain
            # url = 'https://www.baidu.com/s?wd=%22www.baidu.com%22'

            req = urllib2.Request(url, headers = self.bd_headers)
            content = urllib2.urlopen(req).read()

            findList = re.findall(self.bd_pattern, content)
            if len(findList) > 0 :
                print int(str(findList[0]).replace(',', ''))
            else:
                return 0
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度失败,错误原因",e.reason
                return None

    # 导出结果为csv格式
    # def exportCSV(tbody):

    def run(self):
        rank_str = raw_input("请输入反链个数（默认20）:")
        if rank_str != '' :
            self.rank_count = int(rank_str)
        print self.div_line
    
        # 今天日期
        today = datetime.date.today()
        # 一天的时间
        oneday = datetime.timedelta(days=1)
    
        today_1 = (today + oneday*1).strftime("%Y-%m-%d")
        today_2 = (today + oneday*2).strftime("%Y-%m-%d")
        today_3 = (today + oneday*3).strftime("%Y-%m-%d")
        today_4 = (today + oneday*4).strftime("%Y-%m-%d")
    
        date_str = '(1)' + today_1 + '\n(2)' + today_2 + '\n(3)' + today_3 + '\n(4)' + today_4 + '\n请输入查询日期: ';
    
        ins_day = raw_input(date_str)
    
        # 查询日期条件
        if ins_day != '':
            self.day = int(ins_day)
    
        # 获取总条数
        strdata = self.getJsonData()
    
        # print strdata
    
        print self.div_line
    
        jdata = json.loads(strdata);
    
        # 总记录数
        totalCount = jdata['totalCount'];
    
        print '共检索到' + str(totalCount) + '条数据'
    
        print self.div_line
    
        if totalCount > 0 :
            pageCount = totalCount
            # exportCSV(reLoadData())
        else:
            print '没有数据'
            
# 主方法
if __name__ == "__main__":
    dm = DomainSearch()
    dm.run()
