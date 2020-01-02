"""布尔
布尔是整数子类型，也就是说True、False可被当作数字直接使用。

>>> issubclass(bool, int)
True
>>> isinstance(True, int)
True

# 在进行布尔转换时，数字零、空值（None）、空序列和空字典都被视作False，反之为True。
>>> data = (0, 0.0, None, '', list(), tuple(), dict(), set(), frozenset())
>>> any(map(bool, data))  # any: 当 iter 有一个为 True 则返回 Ture ， 否则返回 False
False
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
