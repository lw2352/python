import urllib.request
import re

#打开url地址，并得到html（未进行utf-8解码）
def url_open(url): 
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read()
    #time.sleep(3)
    return html

 #获取图片的url地址，并将其写入文件
def find_imgs():
    html = url_open(url).decode('utf-8')
    #print(html)
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)

    for each in imglist:
        #print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)



if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/4658563357"
    find_imgs()



