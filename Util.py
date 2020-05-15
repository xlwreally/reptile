import requests
import os
import pandas as pd
def ToExcel(list,name):
    Path="C://Users//XLW//Desktop//TEMP//"+name+".xls"
    if (os.path.exists(Path)):
        os.remove(Path)
    dataframe = pd.DataFrame(list)
    dataframe.to_excel(Path)
    print("保存成功")
def getHTMLText(url):
    kv={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    cookie = {
        "cisession": "19dfd70a27ec0eecf1fe3fc2e48b7f91c7c83c60",
        "CNZZDATA100020196": "1815846425-1478580135-https%253A%252F%252Fwww.baidu.com%252F%7C1483922031",
              "Hm_lvt_f805f7762a9a237a0deac37015e9f6d9":"1482722012,1483926313",
                                                        "Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9": "1483926368"
    }
    try: # 网络连接有风险，异常处理很重要
        r = requests.get(url, timeout=30,headers=kv,cookies=cookie)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        text=r.text
        return text
    except:
        return "产生异常"
def getHTMLFile(url):
    kv={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    cookie = {
        "cisession": "19dfd70a27ec0eecf1fe3fc2e48b7f91c7c83c60",
        "CNZZDATA100020196": "1815846425-1478580135-https%253A%252F%252Fwww.baidu.com%252F%7C1483922031",
              "Hm_lvt_f805f7762a9a237a0deac37015e9f6d9":"1482722012,1483926313",
                                                        "Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9": "1483926368"
    }



    try: # 网络连接有风险，异常处理很重要
        root = "C://Users//XLW//Desktop//TEMP//"
        path = root + url.split('/')[-1]
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
                r = requests.get(url, timeout=30,headers=kv,cookies=cookie)
                r.raise_for_status() #如果状态不是200，引发HTTPError异常
                r.encoding = r.apparent_encoding
                text=r.text
                print(len(text))
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("保存成功")
        else:
            print("文件已经存在")
    except:
            print("产生异常")
if __name__ == "__main__":
        # url = "https://www.baidu.com/s?tn=mswin_oem_dg&ie=utf-16&word=py"
        # print(getHTMLText(url))
        # getHTMLFile("https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1-2885cdb57f.png")
        ip="124.89.2.68"
        # str=getHTMLText(r"https://www.ip138.com/iplookup.asp?ip="+ip+"&action=2")
        # begin=str.index("ASN归属地",7000)
        # end=str.index("</font>",begin)
        # print(str[begin+7:end])
        str = getHTMLText(r"http://www.86pm25.com/paiming.htm")
        soup=BeautifulSoup(str,"html.parser")
        print(soup.prettify())

        print("yes")
