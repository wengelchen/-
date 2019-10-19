import requests
from bs4 import BeautifulSoup
import bs4

def GetHtml(url):
    try:
        r=requests.get(url,timeout=30)
        print(r.status_code)
        r.encoding=r.apparent_encoding   #这里写成了r.encoding=r.apparent.encoding导致程序出不来
        return r.text
    except:
        return ' '
def ParseHtml(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find("tbody").children:
         if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    print(ulist)
def PrintList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]       
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
def main():
    uinfo=[];
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html=GetHtml(url)
    unifo=ParseHtml(uinfo,html)
    PrintList(uinfo,20)
main()
    
    
            
    

        
    
    

                           
