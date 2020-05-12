import sys
import bs4
import Util
import re
import threading
import  time
from progressbar import *
from bs4 import *
class findStock(threading.Thread):
    def __init__(self, html,list):
        threading.Thread.__init__(self)
        self.list = list
        self.html = html

    def run(self):
        try:
            str = Util.getHTMLText(self.html).split(",")
            # list.append(str[0].split("\"")[1])
            self.list.append(str[3])
        except IndexError:
            self.list.append("查询失败")
            pass
    pass
def findStockList(html,list):
    soup = BeautifulSoup(Util.getHTMLText(html), "html.parser")
    all=soup.find(id="quotesearch").find_all("ul")
    for li in all[0].find_all("li"):
        each=[]
        each.append("sh"+li.text[-7:-1])
        each.append(li.text[:-8])
        list.append(each)
    for li in all[1].find_all("li"):
        each=[]
        each.append("sz"+li.text[-7:-1])
        each.append(li.text[:-8])
        list.append(each)
    print("已经获取全部股票代码")



def main():
    list=[]
    findStockList(r"http://quote.eastmoney.com/stock_list.html",list)
    thrlist=[]
    widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(), ' ', ETA(), ' ', FileTransferSpeed()]
    n = list.__len__()
    progress = ProgressBar(widgets=widgets,maxval=n)
    progress.start()
    for each in range(0,n):
        thr=(findStock(r"https://hq.sinajs.cn/?_=0.5710357311326326&list="+list[each][0],list[each]))
        thr.start()
        thrlist.append(thr)
        progress.update(each)

    for eachthr in thrlist:
        eachthr.join()

    progress.finish()  #
    print("一共爬到" + list.__len__().__str__() + "条数据")
    Util.ToExcel(list,"Stock")

if __name__ == '__main__':
    main()