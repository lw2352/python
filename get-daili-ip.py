import urllib.request
import re

url = 'http://www.kuaidaili.com/free/inha/'

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


    port = r'<td data-title="PORT">([^"]+\d)</td>'
    portlist = re.findall(port,html)
    for each in portlist:
        print(each)
        #dizhi_write(each)
        #dizhi_write(',')

    #dizhi_write('\n')

    ip = r'<td data-title="IP">([^"]+\d)</td>'
    iplist = re.findall(ip,html) 
    for each in iplist:
        print(each)
        #dizhi_write(each)
        #dizhi_write(',')
        
#写入文件操作
def dizhi_write(dizhi): 
    with open('img_addrs.txt','a') as f:
        f.write(dizhi)

if __name__ == '__main__':
    find_ip()


'''
import requests as req
import re
import pprint as pp

heads={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.kuaidaili.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 5.1)'
}
ssn = req.Session()
ssn.headers = heads

ptn表=re.compile(r'<div[^>]*?id="list".*?'
                r'(<table[^>]*>.*?</table>)',
                re.X|re.S)
ptn行=re.compile(r'<tr[^>]*>.*?</tr>',re.S)
ptn格=re.compile(r'<td[^>]*>(.*?)</td>',re.S)

url = "http://www.kuaidaili.com/free/inha/"
Proxys=[['IP','PORT','类型','响应速度','最后验证时间']]
for i in range(1,6): # 抓取 5 页
    rsp = ssn.get(url+str(i))
    rsp.encodeing='utf-8'
    html = rsp.text
    表=ptn表.findall(html)
    行=ptn行.findall(表[0])
    for td in 行[1:] :
        td=ptn格.findall(td)
        td.pop(4)
        td.pop(2)
        Proxys.append(td)
    
pp.pprint(Proxys)
input('暂停')
'''






#re.search(r'(([01]{0,1}\d{0,1}\d|2[0,4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
