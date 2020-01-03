"""整数

>>> x = 1
>>> type(x)
<class 'int'>
>>> import sys
>>> sys.getsizeof(x)
28
>>> y = 1 << 10000
>>> y
199506311688075838488...792596709376
>>> type(y)
<class 'int'>
>>> sys.getsizeof(y)
1360


对于较长数字，为便于阅读，习惯以千分位进行分隔标记。
但逗号在Python语法中有特殊含义，故改用下画线表示，且不限分隔位数。
>>> 78,654,321
(78, 654, 321)
>>> 78_654_321
78654321
>>> 0b110011  # bin
51
>>> 0o12  # oct
10
>>> 0x64  # hex
100
>>> 0b_11001_1
51



# 转换
>>> bin(100)
'0b1100100'
>>> oct(100)
'0o144'
>>> hex(100)
'0x64'
>>> int('0b1100100', 2)
100
>>> int('0o144', 8)
100
>>> int('0x64', 16)
100
>>> int('64', 16)  # 省略进制前缀
100
>>> int(' 100 ')  # 忽略多余空白符
100
>>> int('\t100\t')
100

## 用 eval 也能完成转换，性能较差
>>> eval('0o114')
76

>>> x = 0x1234
>>> n = (x.bit_length() + 8 - 1)  // 8  #计算按8位对齐所需的字节数
>>> import sys
>>> b = x.to_bytes(n, sys.byteorder)
>>> b.hex()
'3412'
>>> hex(int.from_bytes(b, sys.byteorder))
'0x1234'

>>> 3 / 2
1.5
>>> type(3/2)
<class 'float'>
>>> 4 / 2  # ture division
2.0
>>> 3 // 2  # floor divsion
1



## 如要获取余数，可用取模运算符（mod）或 divmod 函数。
>>> 5 % 2
1
>>> divmod(5, 2)
(2, 1)



## Python 3不再支持数字和非数字类型的比较操作
>>> 1 > ''
Traceback (most recent call last):
    ...
TypeError: '>' not supported between instances of 'int' and 'str'
>>> 1 < []
Traceback (most recent call last):
    ...
TypeError: '<' not supported between instances of 'int' and 'list'
"""


if __name__ == "__main__":
    import doctest
    optionflags = doctest.ELLIPSIS
    doctest.testmod(optionflags=optionflags)
