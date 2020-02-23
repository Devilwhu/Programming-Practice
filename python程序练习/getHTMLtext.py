import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if _name_=="_main_":
    url="http://www.baidu.com"
    print(getHTMLText(url))
    
