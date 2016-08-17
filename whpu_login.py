import urllib.request
import re
import http.cookiejar
import urllib.parse as up
import sys
#cookie = http.cookiejar.CookieJar()
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
#response = opener.open('http://www.baidu.com')

#for item in cookie:  
    #print(item)
#url = 'http://www.zimuzu.tv/user/fav'

headers=('Connection':'Keep-Alive',  
        'Accept': 'text/html, application/xhtml+xml, */*',  
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #'Cookie':'mykeywords=a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22%E6%B8%85%E9%81%93%E5%A4%AB%22%3Bi%3A1%3Bs%3A12%3A%22%E9%BB%91%E5%AE%A2%E5%86%9B%E5%9B%A2%22%3B%7D; last_item:34637=%E5%9B%BD%E7%8E%8B%E7%9A%84%E5%85%A8%E6%81%AF%E5%9B%BE.A.Hologram.for.the.King.2016.720p.BluRay.x264-DRONES.mkv; last_item_date:34637=1470055777; PHPSESSID=p93j1f91vhk7qmcff85pu2k4f4; CNZZDATA1254180690=1846998638-1466726444-%7C1471261904; GINFO=uid%3D3942783%26nickname%3Dlw2352%26group_id%3D1%26avatar_t%3D%26main_group_id%3D0%26common_group_id%3D56; GKEY=3c0cfe1d0c77933a33d56db52c21527f',
        #'Referer':'http://www.zimuzu.tv/user/user/index'
        )

def url_open(url):
    req=urllib.request.Request(url,headers)
    html = urllib.request.urlopen(req)
    html = html.read()
    #print(html)
    return html

def post_data(check_code):
    data = dict()

    data['__VIEWSTATE'] = 'dDwtMTg3MTM5OTI5MTs7PkU5tv6SC3i8arbBXaQUpYX4UT/F'
    data['TextBox1'] = '1304080139'
    data['TextBox2'] = 'sk123654'
    data['TextBox3'] = check_code()
    data['RadioButtonList1'] = '学生'
    
    post_data = up.urlencode(data).encode('utf-8') # 编译post数据
    return post_data

def check_code():
    picture = url_open('http://211.85.192.95/(onwvdg450iu4lj451wjkdw45)/CheckCode.aspx')
    local = open('check_code.png','wb')
    local.write(picture)
    local.close()
    check_code =  input("please input the check code: ")
    return check_code

# cookie上创建一个opener
def build_opener():
    cookie = CookieJar()
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookie_handler)
    print(cookie)
    return opener

def main():
    url = 'http://211.85.192.95/(onwvdg450iu4lj451wjkdw45)/default2.aspx'
    
    req = urllib.Request(url,post_data,headers)
    response = opener.open(req)
    html = response.read()

    test_url = 'http://211.85.192.95/(onwvdg450iu4lj451wjkdw45)/xs_main.aspx?xh=1304080139'
    req = ur.urlopen(testurl)
    print(req.read().decode('gbk2312'))

if __name__ == '__main__':
    check_code = check_code()
    post_data = post_data(check_code)
    opener = build_opener()
    urllib.request.install_opener(opener)
    main()
    

