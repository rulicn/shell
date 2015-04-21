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

# 重新加载所有数据 并计算进度
def reLoadData():
    tbody = ''
    # 重新检索
    jdata = getJsonData().decode('utf-8')

    strdata = json.loads(jdata)

    if len(strdata['data']) > 0:
        for domainkey in strdata['data']:

            rank_num = searchRank(domainkey['Fulldomain'].encode('utf-8'))
            # rank_num = 100

            if rank_num > rank_count:
                tbody += '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>'\
                    .format(domainkey['Fulldomain'].encode('utf-8'), domainkey['BeianNum'].encode('utf-8'),
                            domainkey['Regdate'].encode('utf-8'), domainkey['Deldate'].encode('utf-8'), str(rank_num),
                            domainkey['BdWeight'].encode('utf-8'))

    return tbody

# 查询百度反链
def searchRank(domain):
    try:
        url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=www.' + domain
        # url = 'https://www.baidu.com/s?wd=%22www.baidu.com%22'
        i_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"}

        req = urllib2.Request(url, headers=i_headers)
        content = urllib2.urlopen(req).read()

        reg = r'百度为您找到相关结果约(\d+[,]?\d*)个'
        pattern = re.compile(reg)
        findList = re.findall(pattern, content)
        if len(findList) > 0 :
            print int(str(findList[0]).replace(',', ''))
        else:
            return 0
    except Exception,e:

        print e

# 导出结果为html
def exportHtml(tbody):

    htmlContent = '<html><head><meta charset="utf-8"/><style type="text/css">table{{font-family:"微软雅黑","Trebuchet MS",Arial,Helvetica,sans-serif;width:100%;border-collapse:collapse;width:1000px}}table td,th{{font-size:1em;border:1px solid#98bf21;padding:3px 7px 2px 7px}}table th{{font-size:1.1em;text-align:left;padding-top:5px;padding-bottom:4px;background-color:#A7C942;color:#ffffff}}table tr.alt td{{color:#000000;background-color:#EAF2D3}}</style></head><body><table align="center"><tr><th width="300">域名</th><th width="100">备案号</th><th width="80">原注册</th><th width="50">删除时间</th><th width="80">反链数</th><th width="50">权重</th></tr><tbody>{0}</tbody></table></body></html>'.format(tbody)

    filename = datetime.date.today().strftime("%Y%m%d") + '.html'
    htmlfile = open(filename, 'w')
    htmlfile.write(htmlContent)
    htmlfile.close()


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
        exportHtml(reLoadData())

    else:
        print '没有数据'
