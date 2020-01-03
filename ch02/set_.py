"""集合

# 创建
>>> type({})  # 没有初始化值，表示创建一个空字典
<class 'dict'>
>>> type({'a':1})  # 字典：键值对
<class 'dict'>

## 调用类型构造方法创建，或使用推导式。
>>> set({1, 'a', 1.0})
{1, 'a'}
>>> frozenset(range(3))
frozenset({0, 1, 2})
>>> {x + 1 for x in range(6) if x % 2 == 0}
{1, 3, 5}

## 允许在不同版本间转换。
>>> s = {1}
>>> f = frozenset(s)
>>> set(f)
{1}



# 操作
支持大小、相等运算符。
>>> {1, 2} > {2, 1}
False
>>> {1, 2} == {2, 1}
True

子集判断不能使用in、not in语句，它仅用来检查是否包含某个元素。
>>> {1, 2} <= {1, 2, 3}  # 子集：issubset
True
>>> {1, 2, 3} >= {1, 2}  # 超集：issuperset
True
>>> {1, 2} in {1, 2, 3}  # 判断是否包含{1,2}单一元素
False
>>> 3 in {1, 2, 3}  # 判断是否包含3单一元素
True


## 交并差集运算
>>> {1, 2, 3} & {2, 3, 4}  # 交集：intersection
{2, 3}
>>> {1, 2, 3} | {2, 3, 4}  # 并集：union
{1, 2, 3, 4}
>>> {1, 2, 3} - {2, 3, 4}  # 差集：defference
{1}
>>> {1, 2, 3} ^ {2, 3, 4}  # 对称差集：symetrice_difference
{1, 4}


## 集合运算还可与更新操作一起使用
>>> x = {1, 2}
>>> x |= {2, 3}  # update
>>> x
{1, 2, 3}
>>> x = {1, 2}
>>> x &= {2, 3}  # intersection_update
>>> x
{2}


## 删除操作remove可能引发异常，可改用discard
>>> x = {2, 1}
>>> x.remove(2)
>>> x.remove(2)
Traceback (most recent call last):
    ...
KeyError: 2
>>> x.discard(2)

"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
