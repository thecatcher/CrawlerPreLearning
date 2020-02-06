from bs4 import BeautifulSoup
#
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# html2 = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title.string)
#
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)
#
# """获取名称"""
# # 这个获取的是标签的标签名,并不是标签内容
# print(soup.title.name)
# """获取属性"""
# # 两种方法是一样的
# print(soup.p.attrs['name'])
# print(soup.p['name'])
# """获取标签内容"""
# print(soup.p.string)
# """嵌套选择"""
# print(soup.head.title.string)
#
# """获取相关节点"""
# soup = BeautifulSoup(html2, 'lxml')
#
# # 获取子节点,contents方法返回的是一个列表
# print(soup.p.contents)
# # children的话会返回一个迭代器
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i, child)
# # 获取所有子孙节点
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
#
# # 获取父节点,会打印整个父节点的内容
# print(soup.a.parent)
# # 获取祖先节点,返回值是一个迭代器
# print(list(enumerate(soup.a.parents)))
# # 向下获取兄弟节点
# print(list(enumerate(soup.a.next_siblings)))
# # 向上获取兄弟节点
# print(list(enumerate(soup.a.previous_siblings)))
#

"""标准选择器"""
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
# 通过标签名来选择
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))
# 进行层层标签的查找
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

# 通过参数进行选择
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
# 对于html的一些常见参数,可以直接支持到参数名,而不需要使用attrs
print(soup.find_all(id='list-1'))
print(soup.find_all(class_ = 'element'))
# 通过text进行选择
print(soup.find_all(text='Foo'))

# find方法会返回查找到的第一个标签
print(soup.find('ul'))
print(type(soup.find('ul')))
# 查找不存在的标签会返回None
print(soup.find('page'))

"""CSS选择器"""

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html,'lxml')
# 通过class来进行选择
print(soup.select('.panel .panel-heading'))
# 通过标签进行选择
print(soup.select('ul li'))
print(soup.select('ul')[0])
# 通过标签进行迭代选择
for ul in soup.select('ul'):
    print(ul.select('li'))
# 通过id进行选择
print(soup.select('#list-2 .element'))
# 获取属性的两种方法
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
for li in soup.select('li'):
    print(li.get_text())
