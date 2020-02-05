import urllib.error
import urllib.request

# """demo_1"""
# response = urllib.request.urlopen('http://httpbin.org')
# # print(response.read().decode('utf-8'))
# print(response.info())
# print(response.geturl())
#
#
# """demo_2"""
# data = bytes(urllib.parse.urlencode({"world": "hello"}), encoding="utf8")
# print(data)
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(type(response))
# print(response.read())
#
# """demo_3"""
# try:
#     response = urllib.request.urlopen('http://httpbin.org', timeout=0.1)
#     print(response.read())
# # except urllib.error.URLError as e:
# #     if isinstance(e.reason, socket.timeout):
# #         print("TIME OUT")
# except Exception as e:
#     print(type(e))

"""demo_4 status code and response header"""

response = urllib.request.urlopen("http://www.python.org")
print(response.status)
print(response.getheaders())
print(response.getheader("Server"))
