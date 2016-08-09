import urllib.request
import re

#默认网址:http://www.igxe.cn/productlist-17?page_no=2&sort_key=1&sort_rule=1

def url_open(url):
    req=urllib.request.Request(url,headers={'Connection': 'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
        })
    html = urllib.request.urlopen(req)
    html = html.read() 
    return html

def find_info(url):
    i=0 
    html = url_open(url).decode('utf-8')
    
#找出物品名称
    name=r'<h3 class="h3" style="color:#\S\S\S\S\S\S">([^"]+\s)</h3>'
    name_list=re.findall(name,html)   #name_list是以列表
    print('$物品名称$')
    for each in name_list:
        print(each)

#找出物品磨损级别
    exterior=r'<b>(\w\w\w\w)\s'
    exterior_list=re.findall(exterior,html)
    print('$磨损级别$')
    for each in exterior_list:
        print(each)

#找出物品磨损值
    exterior_num=r'<span>\w\w\w:\s+([^"]+\d)'
    exterior_num_list=re.findall(exterior_num,html)
    print('$磨损值$')
    for each in exterior_num_list:
        print(each)

#找出物品的sale_id
    sale_id=r'<i sale_id="([\d]+\d)'
    sale_id_list=re.findall(sale_id,html)
    print('$sale_id$')
    for each in sale_id_list:
        print(each)

#找出物品市场均价
    market_price=r'<span>\w\w\w\w: <b>([^"]+\d)</b>'
    market_price_list=re.findall(market_price,html)
    print('$市场均价$')
    for each in market_price_list:
        print(each)
    
#找出物品current价
    current_price=r'\w\w\w\w: <strong>([^"]+\d)</strong>'
    current_price_list=re.findall(current_price,html)
    print('$current价$')
    for each in current_price_list:
        print(each)

    
#找出物品价格比例
    print('$比例$')
    rate_list=[]
    while(i<12):
        a = float(market_price_list[i])
        b= float(current_price_list[i])
        rate = int((b/a)*100)
        rate = float(rate/100)
        rate_list.append(rate)
        i+=1
        print(rate)
    #print(rate_list)
        
 #找出N个页面上的信息
def get_info(name_id,pages,money_start,money_end,sort_key,sort_rule):
    j = 1
    while(j<=pages): 
        print(j)
        url = 'http://www.igxe.cn/'+'productlist-'+name_id+'?page_no='+str(j)+'&money_start='+money_start+'&money_end'+money_end+'&sort_key='+sort_key+'&sort_rule='+sort_rule
        print(url)
        find_info(url)  
        j += 1


#写入文件操作
def file_write(dizhi): 
    with open('img_addrs.csv','a') as f:
        f.write(dizhi)

if __name__ == '__main__':
    #get_info()
    print('价格：从低到高--[2,0]  从高到低--[2,1] \n时间：从新到旧--[1,1]  从旧到新--[1,0]')
    name_id= input("Please enter a weapon name_id: " )
    pages = input("How many pages do you wan to get: ")
    money_start = input("Please enter a money_start: " )
    money_end = input("Please enter a money_end: " )
    sort_key = input("Please enter the sort_key: " )
    sort_rule = input("Please enter the sort_rule: " )
    get_info(str(name_id),int(pages),str(money_start),str(money_end),str(sort_key),str(sort_rule))  #通过输入来修改url地址


'''
价格：从低到高  2,0
          从高到低 2,1
时间：从新到旧 1,1
          从旧到新 1,0
'''
