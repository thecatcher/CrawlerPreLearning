import re
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
content = requests.get('https://book.douban.com', headers={'User-Agent': user_agent}).text
if content:
    print("Get web content finished!")
    print("Content length:%d" % len(content))
#   print(content)
pattern = re.compile(
    '<div.*?info.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>', re.S)
print("compile pattern finished!")
print(pattern)
# result = re.search(pattern,content)
results = re.findall(pattern, content[95000:105000])
print(results)
for result in results:
    url,name,author,date = result
    author= re.sub('\s','',author)
    date=re.sub('\s','',date)
    print(url+"\t"+name+"\t"+author+"\t"+date)
