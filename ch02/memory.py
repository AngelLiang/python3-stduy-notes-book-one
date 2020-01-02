"""内存
对于常用的小数字，解释器会在初始化时进行预缓存。
以Python36为例，其预缓存范围是[-5,256]。

>>> a = -5
>>> b = -5
>>> a is b
True
>>> a = 256
>>> b = 256
>>> a is b
True

# 如果超出缓存范围，那么每次都要新建对象。
>>> a = -6
>>> b = -6
>>> a is b
False
>>> a = 257
>>> b = 257
>>> a is b
False

>>> import psutil
>>> def res():
...     m = psutil.Process().memory_info()
...     print(m.rss >> 20, 'MB')
...
>>> res()
17 MB
>>> x = list(range(10000000))
>>> res()
403 MB
>>> del x
>>> res()
17 MB
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
