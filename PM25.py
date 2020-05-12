import sys
import bs4
import Util
import re
from bs4 import *
def findPm(ulist,html):
    begin=html.index("PM2.5浓度")
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find(id="goodtable").children:
        if isinstance(tr, bs4.element.Tag):
            if tr('td') is not None:
                for td in tr('td'):
                    if isinstance(td, bs4.element.Tag):
                        ulist.append(td.text)
        # if isinstance(tr,bs4.element.Tag):
        #     # tds=tr('tr')
        #     ulist.append(tr[0].text)
def printPm(ulist):
    it=ulist.__iter__()
    temp=['排名','城市','省份','AQI','等级','PM2.5']
    print('{0:{6}^2} {1:{6}^10} {2:{6}^10} {3:{6}^5} {4:{6}^5} {5:{6}^5}'.format(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5],chr(12288)))

    while True:
        try:
            for i in range(6):
                temp[i] = it.__next__()
        except StopIteration:
            sys.exit()
        else:
              print('{0:{6}^2} {1:{6}^10} {2:{6}^10} {3:{6}^5} {4:{6}^5} {5:{6}^5}'.format(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],chr(12288)))
    pass
def main():
    str = Util.getHTMLText(r"http://www.86pm25.com/paiming.htm")
    ulist=[]
    findPm(ulist,str)
    printPm(ulist)
if __name__ == '__main__':
    main()