from pyquery import PyQuery as pq

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 字符串初始化
doc = pq(html)
print(doc('li'))

# url初始化
doc = pq(url='http://www.baidu.com')
print(doc('head'))
# 文件初始化
doc = pq(filename='demo.html')
print(doc('li'))

"""基本CSS选择器"""
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
# id:# class:. 标签,什么都不加 层次的话,以空格隔开
print(doc('#container .list li'))

# 选择子元素
items = doc('.list')
print(type(items))
lis = items.find('li')
print(type(lis))
print(lis)
# 可以直接使用children方法获取子元素
lis = items.children()
print(type(lis))
print(lis)
# 也可以在children中使用css选择器
lis = items.children('.active')
print(lis)

# 获取父元素
container = items.parent()
print(type(container))
print(container)
# 获取祖先标签
print(type(items.parents()))
print(items.parents())
# 也可以指定css选择器进行查找响应的祖先标签
print(items.parents('.wrap'))

# 获取兄弟元素
# 注意这个选择器,空格表示内层标签 不带空格表示并列关系
lis = doc('.list .item-0.active')
print(lis.siblings())
# 同样的可以用css选择器
print(lis.siblings('.active'))

# 遍历单个元素
li = doc('.item-0.active')
print(li)

# 遍历多个元素,使用item方法,返回值是一个生成器
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li)

"""获取属性"""
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
a = doc('.item-0.active a')
# print(a)
# 获取标签属性
print(a.attr('href'))
print(a.attr.href)
# 获取文本内容
print(a.text())
# 获取标签内html
li = doc('.item-0.active')
print(li.html())

"""DOM操作"""
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
# remove_class 和 removeClass是同一个方法
li.remove_class('active')
print(li)
# add_class和addClass是同一个方法
li.add_class('active')
print(li)
# 在标签内添加参数
li.attr('name','link')
print(li)
# 在标签内添加css代码
li.css('font-size','14px')
print(li)

html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
# remove方法可以删除指定的标签
wrap.find('p').remove()
print(wrap.text())

"""伪类选择器"""
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc = pq(html)
# 选择第一个子节点
print(doc('li:first-child'))
# 选择最后一个子节点
print(doc('li:last-child'))
# 选择 第二个子节点
print(doc('li:nth-child(2)'))
# 选择大于2的子节点
print(doc('li:gt(2)'))
# 选择偶数类型的子节点
print(doc('li:nth-child(2n)'))
# 选择正文包含'second'的子节点
print(doc('li:contains(second)'))
