name = 'HX'
print('hello,python,', name)
print('hello,python,'+name)
# title()函数
print('hello world,', name.title())
# upper()函数
print(name.upper())
# lower()函数
print(name.lower())

# first_name = 'hu'
# last_name = 'xi'
# # 合并字符串+
# full_name = first_name+' '+last_name
# print(full_name)

# 空格和换行
print('真\t的\t很\t不\t错')
print('真的\n很不错')

# 删除空白函数strip
name = ' hux '
name_r = name.rstrip()
name_l = name.lstrip()
name_a = name.strip()
print(name_r)
print(name_l)
print(name_a)

# 简单运算
num_1 = 3
num_2 = 5
# +
num0 = num_1 + num_2
print(num0)
num1 = sum([num_1, num_2])
print(num1)
# -
num2 = num_1 - num_2
# *
num3 = num_1 * num_2
# **
num4 = num_1 ** num_2
# /
num5 = num_1 / num_2
print(num2, num3, num4, num5)

# 函数str()
weight = 2
message = '这是一头重达' + str(weight) + '吨的非洲象'
print(message)
# input()默认字符串类型
weight = input('输入重量(单位:吨):')
message = '这是一头重达' + weight + '吨的非洲象'
print(message)

# # python之禅
# import this

# # 字符串、列表、字典的切片(取头不取尾)
# animal = 'panda'
# animals = ['panda', 'tiger', 'dolphin', 'lion', 'penguin']
# my_information = {'name': 'huxiang', 'gender': 'male', 'age': 24, 'phonenum': '190098812323'}
# print(animal[0])
# print(animal[1:3])
# print(animal[::-1])
# print(animals[0])
# print(animals[1:3])
# print(animals[::-1])
# print(my_information['name'][::-1])
# print(my_information['age'])
# # 列表、字典的修改
# animals[3] = 'wolf'
# print(animals)
# my_information['phonenum'] = '18301637967'
# print(my_information)
# # 列表末尾添加元素append()
# animals.append('monkey')
# print(animals)
# # 列表中插入元素insert()
# animals.insert(1, 'tortoise')
# print(animals)
# # del语句删除列表元素
# del animals[6]
# print(animals)
# # 使用方法pop()删除元素
# animals_first = animals.pop(0)
# animals_last = animals.pop()
# print(animals)
# print(animals_last)
# # 使用remove删除元素
# animals_rem = 'tiger'
# animals.remove(animals_rem)
# print(animals)
# # 使用sort()对列表永久性排序
# print(animals)
# animals.sort()
# print(animals)
# animals.sort(reverse=True)
# # 使用sorted()对列表临时排序
# print(animals)
# print(sorted(animals))
# print(sorted(animals, reverse=True))
# print(animals)
# # 倒着打印列表
# print(animals)
# animals.reverse()
# print(animals)
# # 函数len()
# print(len(animal))
# print(len(animals))
# print(len(my_information))

# # 遍历列表
# animals = ['panda', 'tiger', 'dolphin', 'lion', 'penguin']
# for animal in animals:
#     print(animal)




# # 函数
# def hello(name):
#     print('hello, ' + name)
#     # return 'hello, ' + name
#
#
# hello('hh')
# # r = hello('hh')
# # print(r)
# def hello():
#     print('hello')
#
#
# hello()


# def mySqrt(x):
#     i = 1
#     if x > 0:
#         while i <= x:
#             if i*i < x:
#                 i = i + 1
#             elif i*i > x:
#                 return i-1
#             else:
#                 return i
#     else:
#         return 0
#
#
# r = mySqrt(100)
# print(r)

# # 高阶函数：一个函数接收另一个函数作为参数
# def func(g, arr):
#     return [g(x) for x in arr]
#
#
# def double(x):
#     return 2 * x
#
#
# r = func(double, [1, 3, 5, 7])
# print(r)
# result = map(double, [1, 3, 5, 7])
# print(result)

# print(__name__)

# def fib1(n):
#     a = 0
#     b = 1
#     fib = []
#     for i in range(n):
#         fib.append(a)
#         a, b = b, a+b
#     return fib
#
#
# print(fib1(10))

# def fib2(n):
#     a, b = 0, 1
#     fib = []
#     while a < n:
#         fib.append(a)
#         a, b = b, a+b
#     return fib


# print(fib2(100))

# # 输出，format()的用法
# # 花括号和其中的字符（称为格式字段）将替换为传递给 str.format() 方法的对象。花括号中的数字可用来表示传递给 str.format() 方法的对象的位置
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))
# # 如果在 str.format() 方法中使用关键字参数，则使用参数的名称引用它们的值
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# # 位置和关键字参数可以任意组合
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# # 如果你有一个非常长的格式字符串，你不想把它拆开，那么你最好是按名称而不是按位置引用变量来进行格式化。 这可以通过简单地传递字典并使用方括号 '[]' 访问键来完成。
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
# # 这也可以通过使用 '**' 符号将 table 作为关键字参数传递。
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# # 这在与内置函数 vars() 结合使用时非常有用，它会返回包含所有局部变量的字典。
# # 例如，下面几行代码生成一组整齐的列，其中包含给定的整数和它的平方以及立方:
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))  # {0:2d}中2d表示对齐第二位

# 关于特殊方法 __init__
# 方法__init__() 是一个特殊的方法，用于对对象进行初始化，每当根据类创建新实例时，Python都会自动运行它
# 每个方法第一个参数都是 self，指向实例本身，也就是说它们是和实例绑定的函数，这也是我们称它们为方法而不是函数的原因

# def plusOne(digits):
#     a = 0
#     for i in range(len(digits)):
#         a += digits[i] * (10**(len(digits)-1-i))
#     a += 1
#     dig = list(int(d) for d in str(a))  # 整数拆分成列表
#     return dig
#
#
# print(plusOne([1, 2, 9]))





# # replace()方法
# s = 'qwertyuio'
# s = s.replace('qwer', 'QWER')
# print(s)

# # sort()方法,该方法会改变原来的列表，而不是返回新的排序列表
# a = [2, 1, 5, 4, 7, 8, 9, 3, 1]
# a.sort()
# print(a)
# sorted()


