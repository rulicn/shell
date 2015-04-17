#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: biezhi

import urllib,urllib2,json,datetime,sys

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

#解析从网络上获取的JSON数据
def praserJsonFile(jsonData):

    value = json.loads(jsonData)
    rootlist = value.keys()
    print rootlist
    print duan
    for rootkey in rootlist:
        print rootkey
    print duan
    subvalue = value[rootkey]
    print subvalue
    print duan
    for subkey in subvalue:
        print subkey,subvalue[subkey]

# 查询百度反链
def searchRank(domain):
    try:
        response = urllib2.urlopen('https://www.baidu.com/s?wd=%22www.' + domain + '%22')
        result = response.read(timout*1000)
        if result == '' :
            return 0
        if result.indexOf("很抱歉，没有找到与") != -1 && page.indexOf("请检查您的输入是否正确") != -1 :
            return 0

        pos = result.indexOf("百度为您找到相关结果约");

        if pos != -1 :
            end_pos = result.indexOf("个</div>", pos)
			transString = result.substring(pos + 11, end_pos)
			if transString.strip() != '' :
				if transString.indexOf(",") != -1 :
					transString = transString.replaceAll(",", "")
				    sLong = long(transString.trim())
					return sLong

        return 0
    except Exception,e:

        print e

# 主方法
if __name__ == "__main__":

    rank_count = int(raw_input("请输入反链个数:"))

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



    else:
        print '没有数据'
        
        
String ss = "啊是大三大四的阿萨德阿萨德阿萨德<>dvsdf第三方的身份斯蒂芬10,400个A<><ASDASD>";
		
Pattern pattern = Pattern.compile("第三方的身份斯蒂芬(\\d+[,]?\\d*)个");
Matcher m = pattern.matcher(ss);
if(m.find()){
	String s = m.group();
	s = s.substring(9).replaceAll(",", "");
	s = s.substring(0, s.length() - 1);
	System.out.println("s = " + s);
}
