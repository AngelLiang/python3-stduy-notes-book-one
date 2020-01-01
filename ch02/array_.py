"""数组
>>> import array
>>> a = array.array('b', [0x11, 0x22, 0x33, 0x44])
>>> memoryview(a).hex()  # 使用内存视图查看，内容嵌入而非指针
'11223344'
>>> a = array.array('i')
>>> a.append(100)
>>> a.append(1.23)
Traceback (most recent call last):
    ...
TypeError: integer argument expected, got float
>>> a = array.array('i', [1, 2, 3])
>>> # a.buffer_info()  # 返回缓冲区的内存地址和长度
...
>>> a.extend(range(100000))  # 最加大量内容后，内存地址和长度变化
>>> # a.buffer_info()
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
