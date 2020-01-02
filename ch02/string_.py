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


# 多个动态字符串拼接，应优先选择 join 或 format 方式。
# 相比于多次加法运算和多次内存分配（字符串是不可变对象），
# join 这类函数（方法）可预先计算出总长度，一次性分配内存，
# 随后直接复制内存数据填充。
# 另一方面，将固定模板内容与变量分离的 format ，更易阅读和维护。
>>> username = 'qyuhen'
>>> datetime = '20170101'
>>> '/data/' + username + '/message/' + datetime + '.txt'  # 糟糕的方式
'/data/qyuhen/message/20170101.txt'
>>> tmpl = '/data/{user}/message/{time}.txt'  # 模板单独维护
>>> tmpl.format(user=username, time=datetime)  # 无须考虑参数的次序
'/data/qyuhen/message/20170101.txt'


>>> 'py' in 'python'
True
>>> 'Py' not in 'python'
True


# 作为序列类型，可使用索引序号访问字符串的单个字符或者某一片段。
>>> s = '0123456789'
>>> s[2]
'2'
>>> s[-1]
'9'
>>> s[2:6]
'2345'
>>> s[2:-2]
'234567'


# 使用两个索引号表示一个序列片段的语法被称作切片（slice），可以此返回字符串子串。
# 无论以哪种方式返回与原字符串内容不同的子串时，都可能会重新分配内存，并复制数据。
>>> s = '-' * 1024
>>> s1 = s[10:100]  # 片段，内容不同
>>> s2 = s[:]  # 内容相同
>>> s3 = s.split(',')[0]  # 内容相同
>>> s1 is s  # 内容不同，构建新对象
False
>>> s2 is s  # 内容相同时，直接引用原字符串对象
True
>>> s3 is s
True


# 转换
>>> s = '汉字'
>>> b = s.encode('utf-16')  # to bytes
>>> b.decode('utf-16')  # to Unicode str
'汉字'


# 如要处理BOM信息，可导入 codecs 模块。
>>> import codecs
>>> s = '汉字'
>>> s.encode('utf-8').hex()
'e6b189e5ad97'
>>> codecs.BOM_UTF16_LE.hex()  # BOM标志
'fffe'
>>> codecs.encode(s, 'utf-16be').hex()  # 按指定BOM转换
'6c495b57'
>>> codecs.encode(s, 'utf-16le').hex()
'496c575b'


# Python 3默认编码不再是ASCII，无须额外设置。
>>> import sys
>>> sys.getdefaultencoding()
'utf-8'
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
