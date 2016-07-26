import urllib.request
import re

url = 'http://www.xicidaili.com/'

def url_open(url): 
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read()
    return html

def find_ip():
    html = url_open(url).decode('utf-8')
    #type = re.search(r'"IP"{1,10}',html)
    #print(type)
    p = re.compile('(([01]{0,1}\d{0,1}\d|2[0,4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])')
    print(p.findall(html))
    

find_ip()






#re.search(r'(([01]{0,1}\d{0,1}\d|2[0,4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
