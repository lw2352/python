import urllib.request
import re

url = 'http://www.igxe.cn/category-4'

def url_open(url): 
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read()
    #print(html)
    return html

def find_info():
    html = url_open(url).decode('utf-8')
    
#找出物品名称
    name=r'<h3 class="h3" style="color:#\S\S\S\S\S\S">([^"]+\s)</h3>'
    name_list=re.findall(name,html)
    print('物品名称')
    for each in name_list:
        print(each)

#找出物品磨损级别
    exterior=r'<b>(\w\w\w\w)\s'
    exterior_list=re.findall(exterior,html)
    print('磨损级别')
    for each in exterior_list:
        print(each)

#找出物品磨损值
    exterior_num=r'<span>\w\w\w:([^"]+\d)'
    exterior_num_list=re.findall(exterior_num,html)
    print('磨损值')
    for each in exterior_num_list:
        print(each)

#找出物品的sale_id
    sale_id=r'<i sale_id="([\d]+\d)'
    sale_id_list=re.findall(sale_id,html)
    print('sale_id')
    for each in sale_id_list:
        print(each)

#找出物品市场均价
    market_price=r'<span>\w\w\w\w: <b>([^"]+\d)</b>'
    market_price_list=re.findall(market_price,html)
    print('市场均价')
    for each in market_price_list:
        print(each)

#找出物品价格比例
    current_price=r'<span class="bili fr">([^"]+\d)'
    current_price_list=re.findall(current_price,html)
    print('比例')
    for each in current_price_list:
        print(each)





if __name__ == '__main__':
    find_info()
