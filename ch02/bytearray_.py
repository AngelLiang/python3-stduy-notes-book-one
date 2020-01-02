"""字节数组


>>> b'abc'
b'abc'
>>> bytes('汉字', 'utf-8')
b'\xe6\xb1\x89\xe5\xad\x97'
>>> a = b'abc'
>>> b = a + b'def'
>>> b
b'abcdef'
>>> b.startswith(b'abc')
True
>>> b.upper()
b'ABCDEF'


# 相比于bytes 的一次性内存分配，bytearray 可按需扩张，
# 更适合作为可读写缓冲区使用。如有必要，还可为其提前分配足够的内存，
# 避免中途扩张造成额外消耗。
>>> b = bytearray(b'ab')
>>> len(b)
2
>>> b.append(ord('c'))
>>> b.extend(b'de')
>>> b
bytearray(b'abcde')


# 同样支持加法、乘法等运算符
>>> b'abc' + b'123'
b'abc123'
>>> b'abc' * 2
b'abcabc'
>>> a = bytearray(b'bac')
>>> a * 2
bytearray(b'bacbac')
>>> a += b'123'
>>> a
bytearray(b'bac123')
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
