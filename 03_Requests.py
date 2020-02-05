import json

import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

response = requests.get('http://httpbin.org/get')
print(response.text)

"""带参数请求"""
response = requests.get("http://httpbin.org/get?name=germey&age=22")

print(response.text)

data = {
    "name": "brady",
    "age": 18
}
# 可以自动拼接参数在GET方法之后
response = requests.get("http://httpbin.org/get", params=data)
print(response.text)

"""json解析"""

response = requests.get("http://httpbin.org/get")
print(type(response.text))
response.json()  # 其实就是调用json.loads()
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

"""获取二进制数据"""
response = requests.get("https://github.com/favicon.ico")
print(type(response.text), type(response.content))
# response.text 是一个字符串
# 而reponse.content 是一个bytes
print(response.text)
print(response.content)
with open("favicon.ico", "wb") as f:
    f.write(response.content)
    f.close()

"""添加header信息"""
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.get("https://zhihu.com/explore", headers=headers)
print(response.text)

"""基本POST请求"""
data = {"name": "brady", "age": 18}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.post("http://httpbin.org/post", data=data, headers=headers)
print(response.text)

"""response属性"""
response = requests.get('https://jianshu.com')

print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)

"""status code判断"""

response = requests.get("http://httpbin.org")
# 注意这个写法,高级玩家,需要好好理解一下
exit() if not response.status_code == requests.codes.ok else print("request successfully")

response = requests.get("http://httpbin.org/hello_123.html")
exit() if not response.status_code == 404 else print("404 not found")

"""文件上传"""
file = {'file': open('favicon.ico', 'rb')}
response = requests.post("http://httpbin.org/post", files=file)
print(response.text)

response = requests.get("https://baidu.com")
print(response.cookies)
for each_key, value in response.cookies.items():
    print(each_key + '=' + value)

"""会话维持,主要用来做模拟登陆"""
requests.get("http://httpbin.org/cookies/set/number/123456789")
response = requests.get("http://httpbin.org/cookies")
print(response.cookies)

"""可以使用Session类,相当于维护了一个会话"""
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
response = s.get("http://httpbin.org/cookies")
print(response.text)

"""证书验证"""
response = requests.get("https://www.12306.cn")
print(response.status_code)

response = requests.get("https://www.12306.cn", verify=False)
print(response.status_code)
# 指定CA证书
response = requests.get("https://www.12306.cn", cert=('/path/server.crt', '/path/key'))
print(response.status_code)

"""代理设置"""
proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "https://127.0.0.1:7890"
}
response = requests.get("https://taobao.com", proxies=proxies)
print(response.status_code)

# 带密码验证的方式
proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)

# socks代理
proxies = {
    "http": "socks5://127.0.0.1:7891",
    "https": "socks5://127.0.0.1:7891"
}
response = requests.get("https://taobao.com", proxies=proxies)
print(response.status_code)

"""超时设置"""
try:
    response = requests.get("http://www.taobao.com", timeout=0.1)
    print(response.status_code)
except requests.exceptions.ReadTimeout:
    print("time out")

"""异常处理"""

try:
    response = requests.get("http://httpbin.org/get", timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')
