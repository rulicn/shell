#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: biezhi

import urllib,urllib2,re,json,datetime,sys,time,csv,os

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
        self.bd_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

    # 获取json数据
    def getJsonData(self):
        try:
            result = None
            post_url = 'http://www.22.cn/ajax/YuDing/liebiao.ashx?t=0.7920176072511822&type=en'
            parameters = {'pageIndex':'1','pageCount': self.pageCount,'position':'1','doublep':'0','digit':'1,2,3','sskt':'1','regyear':'0','deltype':'0','suffix':'.com,.net','day':self.day,'show':'1','type':'0','strlen':'5,15'}
            data = urllib.urlencode(parameters)
            request = urllib2.Request(post_url, data, self.domain_header)
            
            result = urllib2.urlopen(request, timeout=5).read()
        except:
            for i in xrange(4):
                try:
                    result = urllib2.urlopen(request, timeout=5).read()
                except:
                    continue
                else:
                    break
        finally:
            return result


    # 重新加载所有数据 并计算进度
    def reLoadData(self):
        # 重新检索
        jdata = self.getJsonData()
        csvdata = []
        if jdata:
            strdata = json.loads(jdata)

            if len(strdata['data']) > 0:
                bj = len(strdata['data'])
                cur = 0
                for domainkey in strdata['data']:

                    full_domain = domainkey['Fulldomain'].encode('utf-8')

                    rank_num = int(self.searchRank(full_domain))

                    # print full_domain + " == " + str(rank_num)

                    if rank_num >= self.rank_count:
                        csvdata.append( (full_domain, domainkey['BeianNum'].encode('gb2312'),
                                         domainkey['Regdate'], domainkey['Deldate'],
                                         str(rank_num), domainkey['BdWeight'] ) )

                    sys.stdout.write('\r')
                    # 百分比
                    percentage = round(float(cur)/float(bj), 2)*float(100)
                    sys.stdout.write("[%s>%s] %0.2f%s" % ('-'*int(percentage), ' '*(100-int(percentage)), float(percentage), '%'))
                    cur+=1

        return csvdata

    # 查询百度反链
    def searchRank(self, domain):
        try:
            content = ''
            reqUrl = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=www.' + domain
            req = urllib2.Request(reqUrl, headers = self.bd_headers)
            content =urllib2.urlopen(req, timeout=5).read()
        except:
            for i in xrange(4):
                try:
                    content =urllib2.urlopen(req, timeout=5).read()
                except:
                    continue
                else:
                    break
        finally:
            findList = re.findall(self.bd_pattern, content)
            if len(findList) > 0 :
                return str(findList[0]).replace(',', '')
            else:
                return '0'

    # 导出结果为csv格式
    def exportCSV(self, csvdata, starttime):

        if csvdata and len(csvdata) > 0:
            # 文件名称
            filename = datetime.date.today().strftime("%Y%m%d") + '.csv'
            csvfile = file(filename, 'w')
            writer = csv.writer(csvfile)
            writer.writerow([u'域名'.encode('gb2312'), u'备案号'.encode('gb2312'), u'原注册时间'.encode('gb2312'),
                             u'删除时间'.encode('gb2312'), u'反链数'.encode('gb2312'), u'权重'.encode('gb2312')])
            writer.writerows(csvdata)
            csvfile.close()

            endtime = datetime.datetime.now()
            interval=(endtime - starttime).seconds

            print u'\n### 任务完成,用时{0}秒'.format(str(interval))
            print u'### 导出文件地址：{0}'.format(os.getcwd() + os.sep + filename)

    def run(self):
        rank_str = raw_input(u"### 请输入反链个数（默认20）:")
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

        date_str = '(1)' + today_1 + '\n(2)' + today_2 + '\n(3)' + today_3 + '\n(4)' + today_4 + '\n### 请输入查询日期: ';

        ins_day = raw_input(date_str)

        # 查询日期条件
        if ins_day != '':
            self.day = 1 + int(ins_day)

        # 获取总条数
        strdata = self.getJsonData()

        # print strdata

        print self.div_line

        jdata = json.loads(strdata)

        # 总记录数
        totalCount = jdata['totalCount']

        print '### 共检索到' + str(totalCount) + '条数据'

        print self.div_line

        if totalCount > 0 :
            self.pageCount = totalCount
            print u'### 开始检索域名数据'
            starttime = datetime.datetime.now()

            csvdata = self.reLoadData()
            self.exportCSV(csvdata, starttime)
        else:
            print u'### 没有数据'

# 主方法
if __name__ == "__main__":
    ds = DomainSearch()
    ds.run()
