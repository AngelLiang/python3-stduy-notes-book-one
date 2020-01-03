"""函数

# 创建
函数由两部分组成：代码对象持有字节码和指令元数据，负责执行；
函数对象则为上下文提供调用实例，并管理所需的状态数据。

>>> def test(x, y = 10):
...     x += 100
...     print(x ,y)
...
>>> test  # 函数对象
<function test at 0x...>
>>> test.__code__  # 代码对象
<code object test at 0x..., file "...", line 1>


代码对象的相关属性由编译器生成，为只读模式。
存储指令运行所需的相关信息，诸如源码行、指令操作数，以及参数和变量名等。
>>> test.__code__.co_varnames  # 参数及变量名列表
('x', 'y')
>>> test.__code__.co_consts  # 指令常量
(None, 100)
>>> import dis
>>> # dis.dis(test.__code__)
...


与代码对象只关注执行不同，函数对象作为外部实例存在，负责管理运行期状态。
比如上例中的参数默认值，以及动态添加的属性等。
>>> test.__defaults__  # 参数默认值
(10,)
>>> test(1)
101 10
>>> test.abc = 'hello, world'
>>> test.__dict__
{'abc': 'hello, world'}

实际上，def是运行期指令。以代码对象为参数，创建函数实例，并在当前上下文中与指定的名字相关联。
正因如此，可用def以单个代码对象为模板创建多个函数实例。
>>> def make(n):
...     ret = []
...     for i in range(n):
...         def test(): print('hello')
...         print(id(test), id(test.__code__))
...         ret.append(test)
...     return ret
...
>>> make(3)
...
[<function make.<locals>.test at 0x...>, <function make.<locals>.test at 0x...>, <function make.<locals>.test at 0x...>]

在名字空间里，名字仅能与单个目标相关联。如此，就无法实现函数重载（overload）。
另外，作为第一类对象（first-class），函数可作为参数和返回值传递。
>>> def test(op, x, y):
...     return op(x, y)
...
>>> def add(x, y):
...     return x + y
...
>>> test(add, 1, 2)  # 将函数作为参数
3
>>> def test():
...     def hello():
...         print('hello, world!')
...     return hello
...
>>> test()()
hello, world!


# 嵌套
支持函数嵌套，其甚至可与外层函数同名
>>> def test():
...     print('outer test')
...     def test():
...         print('inner test')
...     return test
...
>>> x = test()
outer test
>>> x
<function test.<locals>.test at 0x...>
>>> x()
inner test


# 匿名函数
在Python里，匿名函数的正式名称为lambda表达式。
>>> add = lambda x, y: x + y
>>> add
<function <lambda> at 0x...>
>>> add(1, 2)
3
>>> def test(): pass
>>> a = test
>>> a.__name__
'test'
>>> a
<function test at 0x...>

lambda只有变量引用，没有自己的名字。
>>> test = lambda: None
>>> a = test
>>> a.__name__
'<lambda>'
"""


if __name__ == "__main__":
    import doctest
    optionflags = doctest.ELLIPSIS | doctest.DONT_ACCEPT_BLANKLINE
    doctest.testmod(optionflags=optionflags)
