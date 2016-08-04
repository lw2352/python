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
ptn_biao=re.compile(r'<div[^>]*?id="list".*?'
                r'(<table[^>]*>.*?</table>)',
                re.X|re.S)
ptn_hang=re.compile(r'<tr[^>]*>.*?</tr>',re.S)
ptn_ge=re.compile(r'<td[^>]*>(.*?)</td>',re.S)
url = "http://www.kuaidaili.com/free/inha/"
Proxys=[['IP','PORT','type','speed','last time']]
for i in range(1,6): # 抓取 5 页
    rsp = ssn.get(url+str(i))
    rsp.encodeing='utf-8'
    html = rsp.text
    _biao=ptn_biao.findall(html)
    _hang=ptn_hang.findall(_biao[0])
    for td in _hang[1:] :
        td=ptn_ge.findall(td)
        td.pop(4)
        td.pop(2)
        Proxys.append(td)
    
pp.pprint(Proxys)
input('暂停')
