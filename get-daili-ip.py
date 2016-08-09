import urllib.request
import re


def url_open(url): 
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read()
    return html

def find_ip(url):
    html = url_open(url).decode('utf-8')
    myip = url_open('http://whatismyip.com.tw').decode('utf-8')
    print(myip)

    #port = r'<td data-title="PORT">([^"]+\d)</td>'
    #portlist = re.findall(port,html)
    #for each in portlist:
        #print(each)
        #dizhi_write(each)
        #dizhi_write(',')

    #dizhi_write('\n')

    ip = r'<td data-title="IP">([^"]+\d)</td>'
    iplist1 = re.findall(ip,html) 
    for each in iplist1:
        print(each)
    return iplist1
        #dizhi_write(each)
        #dizhi_write(',')

#获取N个页面上的ip
def get_ip():
    i =1
    iplist2 = []
    url = 'http://www.kuaidaili.com/free/inha/'
    while(i<=5):
        page_url = url+str(i)+'/'
        iplist2 += find_ip(page_url)  #将所有获取的ip放入列表iplist2中
        print(i)
        i += 1

    print(iplist2)
        #dizhi_write('\n')
        
             
        
#写入文件操作
def file_write(dizhi): 
    with open('img_addrs.csv','a') as f:
        f.write(dizhi)

if __name__ == '__main__':
    get_ip()








#re.search(r'(([01]{0,1}\d{0,1}\d|2[0,4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
