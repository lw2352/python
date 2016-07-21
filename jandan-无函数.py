import urllib.request
import os 

def get_page(url):
    
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read().decode('utf-8')
       
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    print (html[a:b])
    return html
        
def find_imgs():
    url = 'http://jandan.net/OOXX/'
    html = get_page(url)
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a +255)
        if b !=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a +9
            
        a = html.find('img src=',b)
        
        for each in img_addrs:
                print(each)

if __name__=="__main__":
    find_imgs()
 

#http://bbs.fishc.com/thread-73691-1-1.html
#http://bbs.fishc.com/thread-72767-1-1.html
#http://bbs.fishc.com/thread-70155-1-1.html
#http://bbs.fishc.com/thread-72796-1-1.html
#http://bbs.fishc.com/thread-61960-2-1.html
#http://bbs.fishc.com/thread-73675-1-1.html
