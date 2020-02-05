import urllib.parse
import urllib.request

"""demo1_urlopen可以传入一个Request对象"""
# request = urllib.request.Request("https://python.org")
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))

# url = "http://httpbin.org/post"
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {'name': 'Germey'}
#
# print(urllib.parse.urlencode(dict))

# data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
# req = urllib.request.Request(url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

proxy_handler = urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:7890',
    'https':'https://127.0.0.1:7890'
})
opener = urllib.request.build_opener(proxy_handler)

response = opener.open('http://httpbin.org/get')
print(response.read())