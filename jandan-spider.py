import urllib.request
import os 

url = 'http://jandan.net/ooxx/'

#打开url地址，并得到html（未进行utf-8解码）
def url_open(url): 
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read()
    return html   

#获得当前网页的页号
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    print (html[a:b])
    return html[a:b]   #页号

 #获取图片的url地址，并将其写入文件
def find_imgs():
    html = url_open(url).decode('utf-8')
    img_addrs = [ ]
    
    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a +255)
        if b !=-1:
            img_addrs.append(html[a+9:b+4]) #  ？
        else:
            b = a +9
            
        a = html.find('img src=',b)
        
        for each in img_addrs:
                dizhi_write(each)
                dizhi_write('\n')
                print (each)    #图片的地址

#写入文件操作
def dizhi_write(dizhi): 
    with open('img_addrs.txt','a') as f:
        f.write(dizhi)
    
find_imgs()
