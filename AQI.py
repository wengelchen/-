import requests
from bs4 import BeautifulSoup
import bs4#为了使用bs4的标签函数
from pandas import DataFrame
#获取页面信息
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        print(r.status_code)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
#将数据存到list中
def fillUnivList(ulist,html):
    ulist=[]
    soup=BeautifulSoup(html,'html.parser')
    for tbody in soup.find_all('tbody')[1:2]:     #注意这里find—all跟find的区别，find返回的是一个单一变量对象，find—all返回的是列表     
            for tr_boy in tbody.find_all('tr'):    
                if isinstance(tr_boy,bs4.element.Tag):
                    text=tr_boy('th')
                    text1=tr_boy('td')
                    ulist.append([text[0].string,text1[0].string])
    for i in range(len(ulist)):
        u=ulist[i]
        print('{:^7}\t{:^1}'.format(u[0],u[1]))
    data=DataFrame(ulist)
    data.to_csv('data.csv',header=False,index=False,mode='a',encoding='utf_8_sig')
    
'''                                                 
    
#将num个list中的数据打印显示出来,可视化输出
def printUnivList(ulist):
    #打印表头
    print('{0:^10}\t{1:^10}'.format('时间','指数',))
    for i in range(len(ulist)):
        print("ok")
        u=ulist[i]
        print('{:^10}\t{:^10}'.format(u[0],u[1]))
    '''
#主函数
def main():
    uinfo=[]#待放入数据的列表
    url='http://www.86pm25.com/city/zhaoqing.html'
    html=getHTMLText(url)
    unifo=fillUnivList(uinfo,html)
   # printUnivList(uinfo)#打印20组数据
main()
