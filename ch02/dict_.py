"""字典
字典是内置类型中唯一的映射（mapping）结构，基于哈希表存储键值对数据。
值可以是任意数据，但主键必须是可哈希类型。


>>> import collections
>>> issubclass(list, collections.Hashable)
False
>>> issubclass(int, collections.Hashable)
True
>>> hash([1, 2, 3])
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'list'
>>> hash((1, 2, [3, 4]))  # 包含可变列表元素
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'list'
>>> callable(list().__hash__)
False



# 构建
>>> {'a': 1, 'b': 2}  # 以大括号键值对方式创建
{'a': 1, 'b': 2}
>>> dict(a=1, b=2)  # 或调用类型构造
{'a': 1, 'b': 2}
>>> kvs = (('a', 1), ['b', 2])  # 初始化键值参数也可以元组、列表等迭代对象方式提供
>>> dict(kvs)
{'a': 1, 'b': 2}
>>> dict(zip('abc', range(3)))
{'a': 0, 'b': 1, 'c': 2}
>>> dict(map(lambda k, v: (k, v + 10), 'abc', range(3)))  #使用 lambda 你们函数过滤数据
{'a': 10, 'b': 11, 'c': 12}
>>> {k: v + 10 for k, v in zip('abc', range(3))}  # 使用推导式处理数据
{'a': 10, 'b': 11, 'c': 12}
>>> a = {'a': 1}
>>> b = dict(a, b=2)  # 在复制 a 内容的基础上，新增键值对
>>> b
{'a': 1, 'b': 2}
>>> c = dict.fromkeys(b, 0)  # 仅用 b 主键，内容另设
>>> c
{'a': 0, 'b': 0}
>>> d = dict.fromkeys(('counter1', 'counter2'), 0)  # 显式提供主键
>>> d
{'counter1': 0, 'counter2': 0}



# 操作
# 字典不是序列类型，不支持序号访问，以主键读取、新增或删除内容。
>>> x = dict(a = 1)
>>> x['a']  # 读取
1
>>> x['b'] = 2  # 修改或新增
>>> x
{'a': 1, 'b': 2}
>>> del x['a']  # 删除
>>> x
{'b': 2}
>>> x = dict(a = 1)
>>> x['b']
Traceback (most recent call last):
    ...
KeyError: 'b'
>>> 'b' in x
False
>>> x.get('b', 100)  # 主键 b 不存在，返回默认值 100
100
>>> x.get('a', 100)  # 主键 a 存在，返回实际内容
1
>>> x = {}
>>> x.setdefault('a', 0)  # 如果有a，那么返回实际内容，否则新增{a:0}键值
0
>>> x
{'a': 0}



# 字典不支持加法、乘法、大小等运算，但可比较内容是否相同。
>>> {'b':2, 'a':1} == {'a':1, 'b':2}
True



# 视图
>>> x = dict(a=1, b=2)
>>> ks = x.keys()  # 主键视图
>>> 'b' in ks  # 判断主键是否存在
True
>>> for k in ks: print(k, x[k])  # 利用视图迭代字典
a 1
b 2
>>> x['b'] = 200  # 修改字典内容
>>> x['c'] = 3
>>> for k in ks: print(k, x[k])  # 视图能同步变化
a 1
b 200
c 3
>>> def test(d):
...     for k, v in d:
...         print(k, v)
...
>>> x = dict(a=1)
>>> d = x.items()
>>> test(d)
a 1



# 视图还支持集合运算，以弥补字典功能上的不足。
>>> a = dict(a=1, b=2)
>>> b = dict(c=1, b=2)
>>> ka = a.keys()
>>> kb = b.keys()
>>> ka & kb  # 交集：在a、b中同时存在
{'b'}
>>> ka | kb  # 并集：在a或b中存在
{'a', 'b', 'c'}
>>> ka - kb  # 差集：仅在a中存在
{'a'}
>>> ka ^ kb  # 对称差集：仅在a或仅在b中出现，相当于“并集-交集”
{'a', 'c'}



# 利用视图集合运算，可简化某些操作。
>>> a = dict(a=1, b=2)
>>> b = dict(b=20, c=3)
>>> ks = a.keys() & b.keys()  # 交集，也就是a中必须存在的主键
>>> a.update({k: b[k] for k in ks})  # 利用交集结果提取待更新的内容
>>> a
{'a': 1, 'b': 20}


# 扩展
# 默认字典（defaultdict）
# 默认字典（defaultdict）类似于 setdefault 包装。
# 当主键不存在时，调用构造参数提供的工厂函数返回默认值。
>>> import collections
>>> d = collections.defaultdict(lambda: 100)
>>> d['a']
100
>>> d['b'] += 1
>>> d
defaultdict(<function <lambda> at 0x...>, {'a': 100, 'b': 101})

# 有序字典（OrderedDict）
# 与内部实现无关，有序字典（OrderedDict）明确记录主键首次插入的次序。
>>> d = collections.OrderedDict()
>>> d['z'] = 1
>>> d['a'] = 2
>>> d['x'] = 3
>>> for k, v in d.items(): print(k, v)
z 1
a 2
x 3

# 计数器（Counter）
# 计数器（Counter）对于不存在的主键返回零，但不会新增。
>>> d = collections.Counter()
>>> d['a']
0
>>> d['b'] += 1
>>> d
Counter({'b': 1})


# 链式字典（ChainMap）
# 链式字典（ChainMap）以单一接口访问多个字典内容，其自身并不存储数据。
# 读操作按参数顺序依次查找各字典，但修改操作（新增、更新、删除）仅针对第一字典。
>>> a = dict(a=1, b=2)
>>> b = dict(b=20, c=30)
>>> x = collections.ChainMap(a, b)
>>> x['b'], x['c']  # 按顺序命中
(2, 30)
>>> for k, v in x.items(): print(k, v)  # 遍历所有字典
a 1
b 2
c 30
>>> x['b'] = 999  # 更新，命中第一字典
>>> x['z'] = 888  # 新增，命中第一字典
>>> x
ChainMap({'a': 1, 'b': 999, 'z': 888}, {'b': 20, 'c': 30})


可利用链式字典设计多层次上下文（context）结构。
合理上下文类型，须具备两个基本特征。
首先是继承，所有设置可被调用链的后续函数读取。
其次是修改仅针对当前和后续逻辑，不应向无关的父级传递。
如此，链式字典查找次序本身就是继承体现。
而修改操作被限制在当前第一字典中，自然也不会影响父级字典的同名主键设置。
>>> root = collections.ChainMap({'a': 1})
>>> child = root.new_child({'b': 200})
>>> child['a'] = 100
>>> child
ChainMap({'b': 200, 'a': 100}, {'a': 1})
>>> child.parents
ChainMap({'a': 1})

"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
