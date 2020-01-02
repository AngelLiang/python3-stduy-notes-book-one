"""元组

>>> a = tuple([1, 'abc'])
>>> a[0] = 100
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment


# 元组使用小括号语法，但要与普通括号区别开来。
>>> a = (1, )  # 仅一个元素的元组
>>> type(a)
<class 'tuple'>
>>> b = (1)
>>> type(b)  # 普通括号
<class 'int'>


# 支持与列表类似的运算符操作。但不能修改，总是返回新对象
>>> (1, 2) + (3, 4)
(1, 2, 3, 4)
>>> (1, 2) * 2
(1, 2, 1, 2)
>>> a = (1, 2, 3)
>>> b = a
>>> a += (4, 5)  # 创建新tuple，而不是修改内容
>>> a
(1, 2, 3, 4, 5)
>>> b
(1, 2, 3)


# 因列表支持插入、删除等修改操作，所以序号无法与元素对象构成固定映射。
# 但元组不同，相同序号总是返回同一对象，故可为序号取个“别名”。
>>> import collections
>>> User = collections.namedtuple('User', 'name, age')  # 创建 User 类型，指定字段
>>> issubclass(User, tuple)  # tuple子类
True
>>> u = User('qyuhen', 60)
>>> u.name, u.age  # 使用字段名访问
('qyuhen', 60)
>>> u[0] is u.name  # 或依旧使用序号
True
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
