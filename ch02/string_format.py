"""字符串的格式化

>>> x = 10
>>> y = 20
>>> f'{x} + {y} = {x + y}'  # f-strings
'10 + 20 = 30'
>>> '{} + {} = {}'.format(x, y, x + y)  # str.format
'10 + 20 = 30'

# 除运算符外，还可以是函数调用。
>>> f'{type(x)}'
"<class 'int'>"

# 手工序号和自动序号
>>> '{0} {1} {0}'.format('a', 10)
'a 10 a'
>>> '{} {}'.format(1, 2)  # 自动序号，不能与手工序号混用
'1 2'

# 主键
>>> '{x} {y}'.format(x=100, y=[1,2,3])
'100 [1, 2, 3]'

# 属性和索引
>>> class User:
...     name = None
>>> x = User()
>>> x.name = 'jack'
>>> '{0.name}'.format(x)  # 对象属性
'jack'
>>> '{0[2]}'.format([1,2,3,4])  # 索引
'3'

# 宽度、补位
>>> '{0:#08b}'.format(5)
'0b000101'

# 数字
>>> '{:06.2f}'.format(1.234)  # 保留两位小数
'001.23'
>>> '{:,}'.format(123456789)  # 千分位
'123,456,789'

# 对齐
>>> '[{:^10}]'.format('abc')  # 居中
'[   abc    ]'
>>> '[{:.<10}]'.format('abc')  # 左对齐，以点填充
'[abc.......]'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
