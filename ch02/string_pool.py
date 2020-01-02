"""字符串的池化

池负责管理实例，使用者只需引用即可。另一潜在的好处是，
从池返回的字符串，只需比较指针就可知道内容是否相同，
无须额外计算。可以用池来提升哈希表等类似结构的查找性能。

字符串池的实现算法很简单，就是简单的字典结构。


>>> import sys
>>> "__name__" is sys.intern('__name__')
True


# 除以常量方式出现的名字和字面量外，动态生成的字符串一样可加入池中。
# 如此可保证每次都引用同一对象，不会有额外的创建和分配操作。
>>> a = 'hello, world!'
>>> b = 'hello, world!'
>>> a is b  # 不同实例
False
>>> sys.intern(a) is sys.intern('hello, world!')  # 相同实例
True


# 当然，一旦失去所有外部引用，池内的字符串对象一样会被回收。
>>> a = sys.intern('hello, world!')
>>> id(a)
...
>>> id(sys.intern('hello, world!'))  # 有外部引用
...
>>> del a  # 删除外部引用后被回收
>>> id(sys.intern('hello, world!'))  # 从id值不同可以看到字符串是新建后入池的
...
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
