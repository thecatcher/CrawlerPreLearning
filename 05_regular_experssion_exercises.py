import re

"""demo1"""
html ='''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
"""search找寻第一个符合的结果"""
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html ,re.S)
# print(result.group())
# if result:
#     print(result.group(1),result.group(2))

# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html ,re.S)
# print(result.group())
# if result:
#     print(result.group(1),result.group(2))

# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html )
# print(result.group())
# if result:
#     print(result.group(1),result.group(2))

"""findall方法"""
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# # 搜索出来的所有结果会返回一个列表
# print(results)
# for result in results:
#     print(result)
#     print(result[0],result[1],result[2])
#
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
# print(results)
# for result in results:
#     print(result[1])

"""sub方法"""
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# content_new = re.sub('\d+','',content)
# content_new = re.sub('\d+','Replacement',content)
# content_new = re.sub('(\d+)',r'\1 8910', content)
# print(content)
# print(content_new)

# html_new = re.sub('<a.*?>|</a>','',html)
# #print(html_new)
# results = re.findall('<li.*?>(.*?)</li>',html_new,re.S)
# #print(results)
# for result in results:
#     print(result.strip())

"""compile方法"""

# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# pattern = re.compile('Hello.*?Demo',re.S)
# result = re.match(pattern,content)
# print(result)