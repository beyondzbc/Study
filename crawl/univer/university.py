# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import bs4


# r=requests.get('https://item.jd.com/100006536488.html')
# print(r.status_code)
# print(r.encoding)
# print(r.text[:1000])

# r=requests.get('https://www.amazon.cn/dp/B07CDZD8B7/ref=lp_1397649071_1_1?s=music-players&ie=UTF8&qid=1569067633&sr=1-1')
# print(r.request.headers)
# print(r.status_code)
# print(r.encoding)
# print(r.text[:1000])

# kv={'user-agent':'Mozilla/5.0'}
# url='https://www.amazon.cn/dp/B07CDZD8B7/ref=lp_1397649071_1_1?s=music-players&ie=UTF8&qid=1569067633&sr=1-1'
# r=requests.get(url,headers=kv)
# print(r.status_code)
# print(r.request.headers)
# print(r.text[:1000])

# r=requests.get('http://python123.io/ws/demo.html')
# demo=r.text
# soup=BeautifulSoup(demo,"html.parser")
# print(soup)
# print('-----------------------')
# print(soup.title)


# 中国最好大学排名
# 技术路线：requests+BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校", "分数"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
        # print("Suc" + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
main()
