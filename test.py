#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: biezhi

import urllib,urllib2,re,json,datetime,sys

#查询多少条
pageCount = 1
#查询那一天的
day = 1
#反链个数
rank_count=20
#分割线
div_line ="--------------------------"
#超时设置
timout=10

# 获取json数据
def getJsonData():
    try:
        #post_url = 'http://www.22.cn/ajax/YuDing/liebiao.ashx?t=0.7920176072511822&type=en'
        post_url = 'http://121.42.158.166/data.txt'
        parameters = {'pageIndex':'1','pageCount':pageCount,'position':'1','doublep':'0','digit':'1,2,3','sskt':'1','regyear':'0','deltype':'0','suffix':'.com,.net','day':day,'show':'1','type':'0','strlen':'5,15'}
        headers = {
            'Origin':'http://www.22.cn',
            #'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Referer':'http://www.22.cn/YuDing/guoji/',
            'X-Requested-With':'XMLHttpRequest',
            'Connection':'keep-alive','RA-Ver':'2.9.0'}

        data = urllib.urlencode(parameters)

        # request = urllib2.Request(post_url, data, headers)

        request = urllib2.Request(post_url)

        response = urllib2.urlopen(request)

        page = response.read(timout*1000)

        return page

    except Exception,e:

        print e


# 查询百度反链
def searchRank(domain):
    try:
        # url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=www.'+ domain +'&rsv_pq=8c33fcdd000070ec&rsv_t=0d06WAQv97zMab5GF%2FBD0xNpMtj1sx0J9WrDet7lY4Us%2BYac4w5pvBGo6eI&rsv_enter=1&ct=0&tfflag=0&gpc=stf%3D'
        url = 'https://www.baidu.com/s?wd=%22www.baidu.com%22'
        response = urllib2.urlopen(url)
        result = response.read(timout*1000)
        if result == '' :
            return 0

        print result

        reg = r'百度为您找到相关结果约(\d+[,]?\d*)个'
        pattern = re.compile(reg)
        findList = re.findall(pattern, result)
        if len(findList) > 0 :
            print int(str(findList[0]).replace(',', ''))
        else:
            return 0
    except Exception,e:

        print e

# 主方法
if __name__ == "__main__":

    rank_str = raw_input("请输入反链个数（默认20）:")

    if rank_str != '' :
        rank_count = int(rank_str)

    print div_line

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
        day = int(ins_day)

    print div_line

    # 获取总条数
    strdata = getJsonData()

    # print strdata

    print div_line

    jdata = json.loads(strdata);

    # 总记录数
    totalCount = jdata['totalCount'];

    print '共检索到' + str(totalCount) + '条数据'

    print div_line

    if totalCount > 0 :
        pageCount = totalCount

        # 重新检索
        jdata = getJsonData()

        print  jdata;

        strdata = json.loads(jdata)


        if len(strdata['data']) > 0:
            for domainkey in strdata['data']:
                rank_num = searchRank(domainkey['Fulldomain'])
                print domainkey['Fulldomain'] + ' ---- ' + str(rank_num)

    else:
        print '没有数据'
