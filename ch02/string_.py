"""字符串
字符串存储Unicode文本，是不可变序列类型。

>>> s = '汉字'
>>> len(s)
2
>>> hex(ord('汉'))  # code point
'0x6c49'
>>> chr(0x6c49)
'汉'
>>> ascii('汉字')  # 对 non-ASCII 进行转义
"'\\\\u6c49\\\\u5b57'"
>>> 'h\x69, \u6C49\U00005B57'
'hi, 汉字'
>>> "It's my life"  # 英文缩写
"It's my life"
>>> 'The report contained the "facts" of the case.'  # 包含引文，避免使用\"转义
'The report contained the "facts" of the case.'
>>> 'hello' ', ' 'world'  # 自动合并多个相邻的字面量
'hello, world'
>>> \"""
... Beautiful is batter than ugly.
... Explicit is better than implicit.
... Simple is better than complex.
... \"""
'\\nBeautiful is batter than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\n'

# 在字面量前添加标志，指示构建特定格式字符串。
>>> f = open(r'.\README.md')  # Windows路径
>>> import re
>>> re.findall(r'\\b\\d+\\b', 'a10 100')  #正则表达式
['100']
>>> type(u'abc')  # 默认str就是unicode，无需添加u前缀
<class 'str'>
>>> type(b'abc')  #构建字节数组
<class 'bytes'>

# 操作
# 支持用加法或乘法运算符拼接字符串。
>>> s = 'hello'
>>> s += ',wrold'
>>> '-' * 10
'----------'

# 多个动态字符串拼接，应优先选择join或format方式。
# 相比于多次加法运算和多次内存分配（字符串是不可变对象），
# join这类函数（方法）可预先计算出总长度，一次性分配内存，
# 随后直接复制内存数据填充。
# 另一方面，将固定模板内容与变量分离的format，更易阅读和维护。
>>> username = 'qyuhen'
>>> datetime = '20170101'
>>> '/data/' + username + '/message/' + datetime + '.txt'  # 糟糕的方式
'/data/qyuhen/message/20170101.txt'
>>> tmpl = '/data/{user}/message/{time}.txt'  # 模板单独维护
>>> tmpl.format(user=username, time=datetime)  # 无须考虑参数的次序
'/data/qyuhen/message/20170101.txt'
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
