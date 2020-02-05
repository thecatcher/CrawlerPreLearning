import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))

"""正则表达式的基本用法"""
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w.*Demo$',content)
print(result)
# result.group() 用于获取配匹配到的结果
print(result.group())
# result.group() 输出配匹配的范围
print(result.span())

"""泛匹配"""
result=re.match("^Hello.*Demo$",content)
print(result)
print(result.group())
print(result.span())

"""匹配目标"""
result = re.match("^Hello\s(\d+).*Demo",content)
print(result)
print(result.group(1))
print(result.span())

"""贪婪配置和非贪婪匹配"""
# 贪婪匹配：.*会匹配尽量长的字符串,直到不能满足条件为止
result = re.match('^He.*(\d+).*Demo$', content)
print(result.group(1))

# 非贪婪匹配:.*?会匹配尽量少的字符串
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1))


"""匹配模式"""
content2 = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$',content2,re.S)
print(result.group(1))

"""转移字符的匹配"""
content = 'price is $5.00'
result = re.match('price is $5.00', content)
result2 = re.match('price is \$5\.00',content)
print(result)
print(result2.group())
"""总结:尽量使用泛匹配、使用括号得到匹配目标、尽量使用非贪婪模式、有换行符就用re.S"""

"""search()方法"""
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)

result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
