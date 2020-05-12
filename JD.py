import sys
import bs4
import Util
from bs4 import *
def trans(list,str):
    soup = BeautifulSoup(str, "html.parser")
    for each in soup(class_="gl-i-wrap"):
        if isinstance(each, bs4.element.Tag):
            # ulist.append(em.text)
            key = each.find("i").text
            value = each.find(class_="p-name p-name-type-2").find("em").text
            value=value.split("\n")
            if value.__len__()==1:
                value=value[0]
            else:
                value=value[1]
            ulist.append([key,value])
            print(key+" "+value)

# print(str)
ulist=[]
for index in range(1,4):
    str = Util.getHTMLText(r"https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&psort=3&psort=3&page="+index.__str__()+"&s=390&click=0")
    trans(ulist,str)

print("一共爬到"+ulist.__len__().__str__()+"条数据")
Util.ToExcel(ulist,"JD")