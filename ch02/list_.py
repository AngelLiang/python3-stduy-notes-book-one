"""列表

>>> x = [1, 2]
>>> x[1]
2

>>> x.insert(0, 0)
>>> x
[0, 1, 2]

>>> x.reverse()
>>> x
[2, 1, 0]

# queue
>>> q = []
>>> q.append(1)  # 向队列追加数据
>>> q.append(2)
>>> q.pop(0)  # 按追加顺序弹出数据
1
>>> q.pop(0)
2


# 构建
>>> [1, 'abc', 3.14]
[1, 'abc', 3.14]
>>> list('abc')  # iterable
['a', 'b', 'c']
>>> list(range(3))
[0, 1, 2]


# 推导式
>>> [x + 1 for x in range(3)]
[1, 2, 3]
>>> [x for x in range(6) if x % 2 == 0]
[0, 2, 4]
>>> d = []
>>> for x in range(6):
...     if x % 2 == 0:
...         d.append(x)
...
>>> d
[0, 2, 4]


>>> list.__bases__
(<class 'object'>,)
>>> import collections
>>> collections.UserList.__bases__
(<class 'collections.abc.MutableSequence'>,)

# 以加法运算符为例，对比不同继承的结果。
>>> class A(list): pass
>>> type(A('abc') + list('de'))  # 返回的是list，而不是A
<class 'list'>
>>> class B(collections.UserList): pass
>>> type(B('abc') + list('de'))  # 返回B类型
<class '__main__.B'>



# 操作
# 用加法运算符连接多个列表，乘法复制内容。
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]
>>> [1, 2] * 2
[1, 2, 1, 2]

# 注意，同是加法（或乘法）运算，但结果却不同。
>>> a = [1, 2]
>>> b = a
>>> a = a + [3, 4]  # 新建列表对象，然后与a关联
>>> a
[1, 2, 3, 4]
>>> b
[1, 2]

# 编译器将“+=”运算符处理成INPLACE_ADD操作，也就是修改原数据，
# 而非新建对象。其效果类似于执行list.extend方法。
>>> a = [1, 2]
>>> b = a
>>> a += [3, 4]  # 直接修改a内容
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
>>> a is b
True


# 判断元素是否存在，习惯使用in，而非index方法。
>>> 2 in [1, 2]
True


# 至于删除操作，可用索引序号指定单个元素，或切片指定删除范围。
>>> a = [0, 1, 2, 3, 4, 5]
>>> del a[5]  # 删除单个元素
>>> a
[0, 1, 2, 3, 4]
>>> del a[1:3]  # 范围删除
>>> a
[0, 3, 4]


# 返回切片时创建新列表对象，并复制相关指针数据到新数组。
# 除所引用目标相同外，对列表自身的修改（插入、删除等）互不影响。
# 复制的是指针（引用），而非目标元素对象。
# 对列表自身的修改互不影响，但对目标元素对象的修改是共享的。
>>> a = [0, 2, 4, 6]
>>> b = a[:2]
>>> a[0] is b[0]  # 复制引用，依然指向同一对象
True
>>> a.insert(1, 1)  # 对a列表的操作，不会影响b
>>> a
[0, 1, 2, 4, 6]
>>> b
[0, 2]


# 列表排序可设定条件，比如按字段或长度等。
>>> import list_
>>> User = list_.User
>>> users = [User(f'user{i}', i) for i in (3, 1, 0, 2)]
>>> users
[user3 3, user1 1, user0 0, user2 2]
>>> users.sort(key=lambda u: u.age)  # 使用 lambda 匿名函数返回排序条件
>>> users
[user0 0, user1 1, user2 2, user3 3]

# 如要返回复制品，可使用 sorted 函数。
>>> d = [3, 0, 2, 1]
>>> sorted(d)  # 同样可指定排序条件，或倒序
[0, 1, 2, 3]
>>> d  # 并未影响原列表
[3, 0, 2, 1]


# 利用 bisect 模块，可向有序列表插入元素。
# 它使用二分法查找适合位置，可用来实现优先级队列或一致性哈希算法。
>>> import bisect
>>> d = [0, 2, 4]
>>> bisect.insort_left(d, 1)  # 插入新元素后，依然保持有序状态
>>> d
[0, 1, 2, 4]
>>> bisect.insort_left(d, 2)
>>> d
[0, 1, 2, 2, 4]
>>> bisect.insort_left(d, 3)
>>> d
[0, 1, 2, 2, 3, 4]
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
