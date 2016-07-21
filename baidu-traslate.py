import urllib.request
import urllib.parse
import json

content = input("请输入需要的内容：")
url = 'http://fanyi.baidu.com/v2transapi'
data = {}
#data['type'] = 'AUTO'

#data['doctype'] = 'json'
#data['keyfrom'] = 'fanyi.web'
#data['ue'] = 'UTF-8'
#data['typoResult'] = 'true'
data['from'] = 'en'
data['to'] = 'zh'
data['query'] = content
data['transtype'] = 'translang'
data['simple_means_flag'] = '3'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
target = json.loads(html)
fanyi = target['trans_result']['data'][0]['dst']
print("翻译结果是:%s"%fanyi)

#print(html)
