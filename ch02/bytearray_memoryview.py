r"""内存视图



>>> a = bytearray([0x10, 0x12, 0x13, 0x14, 0x15, 0x16])
>>> x = a[2:5]  # 引用片段
>>> x
bytearray(b'\x13\x14\x15')
>>> a[3] = 0xEE  # 修改原数据
>>> a
bytearray(b'\x10\x12\x13\xee\x15\x16')
>>> x  # 并未同步发生变更，显然是数据复制
bytearray(b'\x13\x14\x15')


为什么需要引用某个片段，而不是整个对象？
以自定义网络协议为例，通常由标准头和数据体两部分组成。
如要验证数据是否被修改，总不能将整个包作为参数交给验证函数。
这势必要求该函数了解协议包结构，这显然是不合理的设计。
而复制数据体又可能导致重大性能开销，同样得不偿失。

>>> a = bytearray([0x10, 0x12, 0x13, 0x14, 0x15, 0x16])
>>> v = memoryview(a)  # 完整视图
>>> x = v[2:5]  # 视图片段
>>> x.hex()
'131415'
>>> a[3] = 0xee  # 对原数据修改，可通过修改视图观察到
>>> x.hex()
'13ee15'
>>> x[1] = 0x13  # 因引用相同的内存区域，可通过视图修改原数据
>>> a
bytearray(b'\x10\x12\x13\x13\x15\x16')



# 能否通过视图修改数据，须看原对象是否允许。
>>> a = b'\x10\11'  # bytes是不可变类型
>>> v = memoryview(a)
>>> v[1] = 0xEE
Traceback (most recent call last):
    ...
TypeError: cannot modify read-only memory


# 如要复制视图数据，可调用 tobytes、tolist 方法。
# 复制后的数据与原对象无关，同样不会影响视图自身。
>>> a = bytearray([0x10, 0x12, 0x13, 0x14, 0x15, 0x16])
>>> v = memoryview(a)
>>> x = v[2:5]
>>> b = x.tobytes()  # 复制并返回视图数据
>>> a[3] = 0xEE  # 对数据进行修改
>>> b  # 不影响复制数据
b'\x13\x14\x15'
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
