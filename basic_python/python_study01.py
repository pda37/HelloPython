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

# def longestCommonPrefix(strs):
#     if len(strs) == 1:
#         return strs[0]
#     else:
#         b = 0
#         short = len(strs[0])
#         for i in range(len(strs)-1):
#             short = min(short, len(strs[i+1]))
#         if short == 0:
#             return ''
#         else:
#             for j in range(short):
#                 a = 1
#                 for m in range(len(strs)-1):
#                     if strs[m][j] == strs[m+1][j]:
#                         a += 1
#                 if a == len(strs):
#                     b += 1
#                 else:
#                     break
#             print(strs, short, b, strs[0][0:b])
#             return strs[0][0:b]

# def isValid(s):
#     if s == '':
#         return False
#     else:
#         if (len(s) % 2) != 0:
#             return False
#         else:
#             dic = {'(': -1, ')': 1, '{': -2, '}': 2, '[': -3, ']': 3}
#             list_s = list(str(d) for d in s)
#             if dic[list_s[0]] > 0:
#                 return False
#             else:
#                 j = 1
#                 while len(list_s) > 2 and j < len(list_s):
#                     if dic[list_s[0]] > 0:
#                         return False
#                     else:
#                         j = 1
#                         for i in range(len(list_s)-1):
#                             if dic[list_s[i]] + dic[list_s[i+1]] == 0 and dic[list_s[i]] < dic[list_s[i+1]]:
#                                 list_s.pop(i)
#                                 list_s.pop(i)
#                                 break
#                             else:
#                                 j += 1
#                 if not list_s or (dic[list_s[0]] + dic[list_s[1]] == 0 and dic[list_s[0]] < dic[list_s[1]]):
#                     return True
#                 else:
#                     return False
#
#
# print(isValid("{}}{"))


# def isValid(s):
#     if s == '':
#         return False
#     else:
#         if (len(s) % 2) != 0:
#             return False
#         else:
#             while '()' in s or '{}' in s or '[]' in s:
#                 if s[0] == ')' or s[0] == '}' or s[0] == ']':
#                     print(s, s[0], 0)
#                     return False
#                 elif s[-1] == '(' or s[-1] == '{' or s[-1] == '[':
#                     print(s, s[-1], 1)
#                     return False
#                 else:
#                     s = s.replace('()', '')
#                     s = s.replace('{}', '')
#                     s = s.replace('[]', '')
#             print(s)
#             return s == ''
#
#
# print(isValid("{}"))

# # replace()方法
# s = 'qwertyuio'
# s = s.replace('qwer', 'QWER')
# print(s)

# # sort()方法,该方法会改变原来的列表，而不是返回新的排序列表
# a = [2, 1, 5, 4, 7, 8, 9, 3, 1]
# a.sort()
# print(a)
# sorted()

# def isPalindrome(x):
#     if x < 0:
#         return False
#     else:
#         li = list(int(a) for a in str(x))
#         j = int(len(li)/2)
#         k = 0
#         for i in range(j):
#             if li[i] != li[len(li)-1-i]:
#                 return False
#             else:
#                 k += 1
#         if k == j:
#             return True

# def isPalindrome(x):
#     if x < 0:
#         return False
#     else:
#         str1 = str(x)
#         str2 = str1[::-1]
#         print(str1, str2)
#         return str1 == str2
#
#
# print(isPalindrome(1234321))

# def climbStairs(n):
#     a, b = 1, 1
#     for i in range(n):
#         a, b = b, a+b
#     return a


# print(climbStairs(3))

# def generate(numRows):
#     # 1=<numRows<=30
#     li = [[1]]
#     for i in range(numRows-1):
#         li[i].insert(0, 0)
#         li[i].append(0)
#         li.append([])
#         for j in range(len(li[i])-1):
#             li[i+1].append(li[i][j]+li[i][j+1])
#     for i in range(numRows-1):
#         li[i].pop()
#         li[i].pop(0)
#     return li
#
#
# def getRow(rowIndex):
#     # 0=<rowIndex<=33
#     li = [[1]]
#     for i in range(rowIndex):
#         li[i].insert(0, 0)
#         li[i].append(0)
#         li.append([])
#         for j in range(len(li[i])-1):
#             li[i+1].append(li[i][j]+li[i][j+1])
#     return li[rowIndex]
#
#
# print(generate(10))
# print(getRow(9))

# def singleNumber(nums):
#     for i in nums:
#         while nums.count(i) == 1:
#             return i
#
#
# print([1, 2, 3, 4, 5, 5, 6, 7])

# def isPalindrome(s):
#     s1 = s.lower()
#     li = list(s1)
#     for i in range(len(li)):
#         if ord(li[i]) < 48 or 57 < ord(li[i]) < 97 or ord(li[i]) > 122:
#             li[i] = ''
#     s2 = ''.join([str(d) for d in li])
#     print(s2)
#     return s2 == s2[::-1]


# import re
# def isPalindrome(s):
#     # s1 = s.lower()
#     s1 = re.sub('[^a-z0-9]', '', s.lower())
#     return s1 == s1[::-1]
#
# 
# print(isPalindrome("asdfg/'hjkl;;lkjg,./fdsa"))

# def isHappy(n):
#     happy = [n]
#     i = 0
#     m = 0
#     while m != 1:
#         li = list(int(a) for a in str(happy[i]))
#         for j in range(len(li)):
#             m += li[j]**2
#         print(m)
#         if m == 1:
#             return True
#         elif m in happy:
#             return False
#         else:
#             happy.append(m)
#             print(happy)
#             i += 1
#             m = 0
#
#
# print(isHappy(68))

# def isPowerOfThree(n):
#     if n <= 0:
#         return False
#     elif n == 1:
#         return True
#     else:
#         while n > 1:
#             if n % 3 != 0:
#                 return False
#             n /= 3
#             print(n)
#         return n == 1
#
#
# print(isPowerOfThree(45))

# def findPoisonedDuration(timeSeries, duration):
#     if len(timeSeries) == 1:
#         return duration
#     else:
#         time = 0
#         for i in range(len(timeSeries)-1):
#             if timeSeries[i+1] - timeSeries[i] >= duration:
#                 time += duration
#             else:
#                 time += (timeSeries[i+1] - timeSeries[i])
#         time += duration
#         return time
#
#
# print(findPoisonedDuration([33, 234], 23434))

# def canPlaceFlowers(flowerbed, n):
#     if n > (len(flowerbed)+1)/2:
#         return False
#     else:
#         flowerbed.insert(0, 0)
#         flowerbed.append(0)
#         print(flowerbed)
#         m = 0
#         for i in range(1, len(flowerbed)-1):
#             if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#                 flowerbed[i] = 1
#                 m += 1
#         print(m, flowerbed)
#         return m >= n
#
#
# print(canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))

"""
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释: 
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
"""


# def largestTriangleArea(points):
#     s_max = 0
#     for i in range(len(points)-2):
#         for j in range(i+1, len(points)-1):
#             for k in range(j+1, len(points)):
#                 a = points[i][0]
#                 b = points[i][1]
#                 c = points[j][0]
#                 d = points[j][1]
#                 e = points[k][0]
#                 f = points[k][1]
#                 s = abs(a*d+b*e+c*f-a*f-b*c-d*e)/2
#                 s_max = max(s_max, s)
#     return s_max


# def largestTriangleArea(points):
#     l_max = 0
#     h_max = 0
#     s_max1 = 0
#     s_max2 = 0
#     a1, b1, c1, d1, a2, b2, c2, d2 = 0, 0, 0, 0, 0, 0, 0, 0
#     for i in range(len(points)-1):
#         for j in range(i+1, len(points)):
#             if abs(points[i][0]-points[j][0]) > l_max:
#                 a1 = points[i][0]
#                 b1 = points[i][1]
#                 c1 = points[j][0]
#                 d1 = points[j][1]
#                 l_max = abs(points[i][0]-points[j][0])
#             if abs(points[i][1]-points[j][1]) > h_max:
#                 a2 = points[i][0]
#                 b2 = points[i][1]
#                 c2 = points[j][0]
#                 d2 = points[j][1]
#                 h_max = abs(points[i][0]-points[j][0])
#     print(a1, b1, c1, d1, a2, b2, c2, d2)
#     # 需要去掉已选中的两点
#     for k in points:
#         e = k[0]
#         f = k[1]
#         if a1 != e and c1 != e and b1 != f and d1 != f:
#             s1 = abs(a1 * d1 + b1 * e + c1 * f - a1 * f - b1 * c1 - d1 * e) / 2
#             s_max1 = max(s_max1, s1)
#         if a2 != e and c2 != e and b2 != f and d2 != f:
#             s2 = abs(a2 * d2 + b2 * e + c2 * f - a1 * f - b2 * c2 - d2 * e) / 2
#             s_max2 = max(s_max2, s2)
#     return max(s_max1, s_max2)
#
#
# print(largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))

# 请对输入的数组 就地 进行上述修改，不要从函数返回任何东西
# def duplicateZeros(arr):
#     k = len(arr)
#     d = []
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             d.append(i)
#     a = 0
#     for j in range(len(d)):
#         if d[j]+a < k:
#             arr.insert(d[j]+a, 0)
#             a += 1
#             del arr[-1]
#     return arr
#
#
# print(duplicateZeros([0, 11, 0, 0, 0, 4]))

# def numEquivDominoPairs(dominoes):
#     if len(dominoes) == 1:
#         return 0
#     else:
#         a = 0
#         for i in range(len(dominoes)-1):
#             for j in range(i+1, len(dominoes)):
#                 if dominoes[i] == dominoes[j] or dominoes[i] == dominoes[j][::-1]:
#                     a += 1
#         return a
#
#
# print(numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6], [3, 4], [1, 2]]))

# def distanceBetweenBusStops(distance, start, destination):
#     distance1, distance2 = 0, 0
#     a = len(distance)
#     distance.extend(distance)
#     if start > destination:
#         start, destination = destination, start
#     for i in range(start, destination):
#         distance1 += distance[i]
#     for j in range(start + a, destination, -1):
#         distance2 += distance[j - 1]
#     return min(distance1, distance2)
#
#
# print(distanceBetweenBusStops(distance=[1, 2, 3, 4], start=2, destination=2))

# def isPathCrossing(path):
#     a, b = 0, 0
#     path_l = [[0, 0]]
#     for i in range(len(path)):
#         if path[i] == 'N':
#             b += 1
#         elif path[i] == 'S':
#             b -= 1
#         elif path[i] == 'E':
#             a += 1
#         elif path[i] == 'W':
#             a -= 1
#         if [a, b] not in path_l:
#             path_l.append([a, b])
#         else:
#             return True
#     return path_l
#
#
# print(isPathCrossing("NES"))

# def decrypt(code, k):
#     if k == 0:
#         return [0]*len(code)
#     else:
#         length = len(code)
#         code1 = []
#         code.extend(code)
#         s = 0
#         if k > 0:
#             for i in range(length):
#                 for j in range(i+1, i+k+1):
#                     s += code[j]
#                 code1.append(s)
#                 s = 0
#         else:
#             for i in range(length):
#                 for j in range(length+i-1, length+i+k-1, -1):
#                     s += code[j]
#                 code1.append(s)
#                 s = 0
#     return code1
#
#
# print(decrypt([5, 7, 1, 4], 3))

# import math
# def arrangeCoins(n):
#     return int((math.sqrt(8*n+1)-1)/2)
#
#
# print(arrangeCoins(4))

# def largestSumAfterKNegations(nums, k):
#     nums.sort()
#     max_sum = 0
#     for i in range(k):
#         if nums[0] >= 0 and (k-i) % 2 == 0:
#             break
#         else:
#             nums[0] = -nums[0]
#             nums.sort()
#     print(nums)
#     for num in nums:
#         max_sum += num
#     return max_sum
#
#
# print(largestSumAfterKNegations([-8, 3, -5, -3, -5, -2], 6))

# def masterMind(solution, guess):
#     real, fake = 0, 0
#     solution_list = []
#     guess_list = []
#     for i in range(len(solution)):
#         if solution[i] == guess[i]:
#             real += 1
#         else:
#             solution_list.append(solution[i])
#             guess_list.append(guess[i])
#     print(real, solution_list, guess_list)
#     for s in guess_list:
#         if s in solution_list:
#             fake += 1
#             solution_list.remove(s)
#     return [real, fake]
#
#
# print(masterMind("RRWR", "RWRR"))

# def thousandSeparator(n: int):
#     n_list = list(a for a in str(n))
#     m = 0
#     for i in range(3, len(n_list), 3):
#         n_list.insert(-i-m, ".")
#         m += 1
#     n_str = "".join(n_list)
#     return n_str
#
#
# print(thousandSeparator(1))

# import math
# def primeNumberArrangement(n):
#     composite_number = []
#     prime_number = list(k for k in range(1, n+1))
#     # print(prime_number)
#     for i in range(3, n+1):
#         for j in range(2, math.ceil(math.sqrt(i))+1):
#             if i % j == 0:
#                 composite_number.append(i)
#                 break
#     # print(composite_number)
#     for num in composite_number:
#         prime_number.remove(num)
#     return prime_number
#
#
# print(primeNumberArrangement(100000))

# def checkPerfectNumber(num):
#     if num == 1:
#         return False
#     else:
#         a = 0
#         i = 1
#         while i < (int(num/i)+1):
#             if num % i == 0:
#                 a += i + (num/i)
#                 i += 1
#             else:
#                 i += 1
#         return num == (a - num)
#
#
# print(checkPerfectNumber(99999994))

# def isPerfectSquare(num):
#     a = 1
#     b = num / a
#     while a < b:
#         a += 1
#         b = num / a
#     return a == b
#
#
# print(isPerfectSquare(20000))

# def findContentChildren(g, s):
#     g.sort()
#     s.sort()
#     n = 0
#     for i in range(len(s)):
#         if not g:
#             break
#         elif s[i] >= g[0]:
#             g.pop(0)
#             n += 1
#     print(g, s, n)
#     return n
#
#
# print(findContentChildren([1, 2], [1, 2, 3]))

# def dominantIndex(nums):
#     a, b, a_index = 0, 0, 0
#     for i in range(len(nums)):
#         if nums[i] >= a:
#             a, b = nums[i], a
#             a_index = i
#         elif nums[i] >= b:
#             b = nums[i]
#     print(a, b)
#     if a >= 2*b:
#         return a_index
#     else:
#         return -1
#
#
# print(dominantIndex([0, 0, 3, 2]))

# def threeSum(nums):
#     if len(nums) < 3:
#         return []
#     else:
#         nums.sort()
#         print(nums)
#         nums_three = []
#         smallest_two = nums[0] + nums[1]
#         zero_index = len(nums) - 1
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 break
#             elif i > 0 and nums[i] == nums[i-1]:
#                 continue
#             else:
#                 for j in range(i + 1, len(nums)-1):
#                     if nums[i] + nums[j] > 0:
#                         break
#                     elif j-i > 1 and nums[j] == nums[j-1]:
#                         continue
#                     elif nums[i] + nums[j] < smallest_two:
#                         for k in range(len(nums)-1, zero_index-1, -1):
#                             if nums[i] + nums[j] + nums[k] < 0:
#                                 break
#                             elif k-j > 1 and k < len(nums)-1 and nums[k] == nums[k+1]:
#                                 continue
#                             elif nums[i] + nums[j] + nums[k] > 0:
#                                 continue
#                             else:
#                                 nums_three.append([nums[i], nums[j], nums[k]])
#                                 zero_index = k
#                                 smallest_two = nums[i] + nums[j]
#                                 break
#                     else:
#                         for k in range(zero_index, j, -1):
#                             if nums[i] + nums[j] + nums[k] < 0:
#                                 break
#                             elif k-j > 1 and k < zero_index-1 and nums[k] == nums[k-1]:
#                                 continue
#                             elif nums[i] + nums[j] + nums[k] > 0:
#                                 continue
#                             else:
#                                 nums_three.append([nums[i], nums[j], nums[k]])
#                                 zero_index = k
#                                 smallest_two = nums[i] + nums[j]
#                                 break
#         return nums_three


# print(threeSum([-7,-4,-4,-2,0,4,4,5,7,7,9,9]))

# def threeSum(nums):
#     if len(nums) < 3:
#         return []
#     else:
#         nums.sort()
#         nums_three = []
#         for i in range(len(nums)-2):
#             left_index = i + 1
#             right_index = len(nums) - 1
#             if nums[i] > 0:
#                 break
#             elif i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             else:
#                 while left_index < right_index:
#                     three_sum = nums[i] + nums[left_index] + nums[right_index]
#                     if three_sum > 0:
#                         right_index -= 1
#                     elif three_sum < 0:
#                         left_index += 1
#                     elif three_sum == 0:
#                         nums_three.append([nums[i], nums[left_index], nums[right_index]])
#                         while right_index > left_index and nums[left_index] == nums[left_index + 1]:
#                             left_index += 1
#                         while left_index < right_index and nums[right_index] == nums[right_index - 1]:
#                             right_index -= 1
#                         left_index += 1
#                         right_index -= 1
#         return nums_three
#
#
# print(threeSum([0,0,0]))

# def numEquivDominoPairs(dominoes) -> int:
#     dic = {}
#     for i in range(len(dominoes)):
#         if dominoes[i][0] > dominoes[i][1]:
#             dominoes[i] = dominoes[i][::-1]
#         if str(dominoes[i]) in dic:
#             dic[str(dominoes[i])] += 1
#         if str(dominoes[i]) not in dic:
#             dic[str(dominoes[i])] = 1
#     print(dic)
#     ans = 0
#     for k in dic:
#         if dic[k] > 1:
#             ans += dic[k]*(dic[k]-1)/2
#     return ans
#
# 
# print(numEquivDominoPairs([[6, 7], [1, 2], [2, 1], [3, 4], [5, 6], [4, 3]]))

# def convert(s, numRows):
#     if numRows == 1:
#         return s
#     else:
#         ans = []
#         for i in range(numRows):
#             ans.append([])
#         for j in range(len(s)):
#             remainder = j % (numRows*2-2)
#             if remainder < numRows:
#                 ans[remainder].append(s[j])
#                 print(ans)
#             else:
#                 remainder -= numRows-2
#                 ans[-remainder].append(s[j])
#                 print(ans)
#         h = ''
#         for k in range(numRows):
#             h += ''.join(ans[k])
#         return h
#
#
# print(convert('Pqwerty.,,uiopasd,.fghjklzxcvbnm', 10))

# # 不使用除法，乘法，mod做除法运算
# def divide(dividend, divisor):
#     a = abs(dividend)
#     b = abs(divisor)
#     ans = 0
#     while a >= b:
#         n = 1
#         c = b
#         while a >= c >= b:
#             a -= c
#             ans += n
#             c += b
#             n += 1
#     if divisor * dividend > 0:
#         if ans <= 2147483647:
#             return ans
#         else:
#             return 2147483647
#     else:
#         ans = -ans
#         if -2147483648 <= ans:
#             return ans
#         else:
#             return 2147483647
#
#
# print(divide(-2147483649, 1), -2147483648/1)
# print(2**31)

# def nextPermutation(nums):
#     n = len(nums)
#     a = 0
#     for i in range(n-1, 0, -1):
#         if nums[i-1] < nums[i] and a == 0:
#             for j in range(n-1, i-1, -1):
#                 if nums[j] > nums[i-1]:
#                     nums[i-1], nums[j] = nums[j], nums[i-1]
#                     print(nums)
#                     a += 1
#                     s = sorted(nums[i:n])
#                     print(s)
#                     for k in range(len(s)):
#                         nums[i+k] = s[k]
#                     break
#     print(nums)
#     if a == 0:
#         for k in range(int(n/2)):
#             nums[k], nums[n - 1 - k] = nums[n - 1 - k], nums[k]
#     print(nums, a)
#
#
# print(nextPermutation([1, 2, 3]))
# print(nextPermutation([3, 2, 1]))

# # 不用sort()，实现sort()
# def sortColors(nums):
#     # nums.sort()
#     # print(nums)
#
#
#
# print(sortColors([2, 1, 1, 0, 2]))

# def largestNumber(nums):
#     s = list(str(a) for a in nums)
#     n = len(str(max(nums)))
#     for i in range(len(s)):
#         while len(s[i]) < n:
#             s[i] = s[i] + s[i][0]
#     h = list(int(a) for a in s)
#     sor0 = []
#     sor1 = []
#     for j in range(len(h)):
#         if h[j] == 0:
#             sor1.append(j)
#     while max(h) > 0:
#         ind = h.index(max(h))
#         sor0.append(ind)
#         h[ind] = 0
#     sor0.extend(sor1)
#     ans = ''
#     for k in range(len(sor0)):
#         ans += str(nums[sor0[k]])
#     return ans

# def largestNumber(nums):
#     if max(nums) == 0:
#         return '0'
#     else:
#         s = list(str(a) for a in nums)
#         for i in range(len(s)-1):
#             for j in range(i+1, len(s)):
#                 if s[i] + s[j] < s[j] + s[i]:
#                     s[i], s[j] = s[j], s[i]
#         ans = ''.join(s)
#         return ans
#
#
#
# print(largestNumber([0, 0]))

# def uniquePaths(m, n):
#     ans = 1
#     if m > n:
#         # 一共要向右走m-1步，向下走n-1步，共m+n-2步
#         # 共有多少走的方法，看作是在m+n-2步中选择n-1步
#         for i in range(n-1):
#             ans *= m+i
#             ans /= n-1-i
#         return round(ans, 0)
#     else:
#         for i in range(m-1):
#             ans *= n+i
#             ans /= m-1-i
#         return round(ans)
#
#
# print(uniquePaths(10, 10))

# def canJump(nums):
#     if nums[0] == 0 and len(nums) > 1:
#         return False
#     else:
#         n = 0
#         for i in range(len(nums)-2, 0, -1):
#             if nums[i] == 0:
#                 for j in range(0, i):
#                     if nums[j] > i - j:
#                         n = 0
#                         print(n)
#                         break
#                     else:
#                         n += 1
#                 if n == i:
#                     return False
#         return True
#
#
# print(canJump([2, 0, 0]))

# def isNStraightHand(hand, groupSize):
#     if len(hand) % groupSize != 0:
#         return False
#     else:
#         while hand:
#             for i in range(int(len(hand)/groupSize)):
#                 m = min(hand)
#                 a = 0
#                 while a < groupSize:
#                     if m in hand:
#                         hand.remove(m)
#                         m += 1
#                         a += 1
#                     else:
#                         return False
#         return not hand
#
#
# print(isNStraightHand([1,2,3,6,2,3,4,7,9], 3))

# def findLucky(arr):
#     ans = -1
#     for a in arr:
#         if a == ans:
#             continue
#         elif arr.count(a) == a:
#             ans = max(ans, a)
#     return ans
#
#
# print(findLucky([1, 2, 2, 4]))

# def canMakeArithmeticProgression(arr):
#     arr.sort()
#     interval = arr[1] - arr[0]
#     for i in range(1, len(arr)-1):
#         if arr[i+1] - arr[i] != interval:
#             return False
#     return True
#
#
# print(canMakeArithmeticProgression([3,2,1,4]))

# def jump(nums):
#     n = len(nums) - 1
#     a = n
#     ans = 0
#     while n > 0:
#         for i in range(n - 1, max(-1, n - 1001), -1):
#             if nums[i] >= n - i:
#                 a = i
#         n = a
#         ans += 1
#     return ans
#
#
# print(jump([6, 3, 0, 1, 4]))

# def findMedianSortedArrays(nums1, nums2):
#     nums = nums1 + nums2
#     nums.sort()
#     print(nums)
#     if len(nums) % 2 == 1:
#         return float(nums[int((len(nums)-1)/2)])
#     else:
#         return float((nums[int(len(nums)/2)]+nums[int(len(nums)/2-1)])/2)
#
#
# print(findMedianSortedArrays([1], []))

# def findTheDifference(s, t):
#     t_list = list(t)
#     print(t_list)
#     for a in s:
#         if a in t_list:
#             t_list.remove(a)
#         else:
#             return a
#     return t_list[0]
#
#
# print(findTheDifference('asdfgh', 'asdlfgh'))

# import math
# def numPrimeArrangements(n: int):
#     non_prime = 1
#     for i in range(3, n+1):
#         for j in range(2, int(math.sqrt(i))+1):
#             if i % j == 0:
#                 non_prime += 1
#                 break
#     ans = 1
#     for i in range(1, non_prime+1):
#         ans *= i
#     for i in range(1, n - non_prime + 1):
#         ans *= i
#     return ans % (10**9+7)
#
#
# print(numPrimeArrangements(100))

# import math
# def countTriples(n: int):
#     ans = 0
#     for c in range(2, n+1):
#         for a in range(1, c):
#             b = int(math.sqrt(c**2 - a**2))
#             if a**2 + b**2 == c**2:
#                 ans += 1
#     return ans
#
#
# print(countTriples(10))

# # 使用缓存通过 动态规划 计算 斐波那契数列 的例子
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
#
# print(fibonacci(100))

# def maximumPopulation(logs):
#     alive = {}
#     for i in range(len(logs)):
#         for j in range(logs[i][0], logs[i][1]):
#             if j not in alive:
#                 alive[j] = 1
#             else:
#                 alive[j] += 1
#     print(alive)
#     alive_order = sorted(alive.items(), key=lambda ali: (ali[1], -ali[0]), reverse=True)
#     print(alive_order)
#     return alive_order[0][0]
#
#
# print(maximumPopulation([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]))

# def diagonalSum(mat):
#     n = len(mat)
#     ans = 0
#     for i in range(n):
#         if i != n-1-i:
#             ans += mat[i][i] + mat[i][n-1-i]
#         else:
#             ans += mat[i][i]
#     return ans
#
#
# print(diagonalSum([[1,1,1],[1,1,1],[1,1,1]]))

# def totalMoney(n: int) -> int:
#     a = int(n / 7)
#     b = n % 7
#     print(a, b)
#     ans = 0
#     for i in range(1, a+1):
#         for j in range(i, i+7):
#             ans += j
#     for k in range(1, b+1):
#         ans += a+k
#     return ans
#
#
# print(totalMoney(10))

# def countBalls(lowLimit, highLimit):
#     ans = {}
#     for i in range(lowLimit, highLimit+1):
#         m = 0
#         num = str(i)
#         for n in num:
#             m += int(n)
#         if m in ans:
#             ans[m] += 1
#         else:
#             ans[m] = 1
#     ans_order = sorted(ans.items(), key=lambda a: a[1], reverse=True)
#     return ans_order[0][1]
#
#
# print(countBalls(5, 15))

# def numWaterBottles(numBottles, numExchange):
#     empty_bottles = 0
#     ans = 0
#     while numBottles > 0:
#         ans += numBottles
#         empty_bottles += numBottles
#         numBottles = 0
#         while empty_bottles >= numExchange:
#             numBottles += int(empty_bottles / numExchange)
#             empty_bottles -= numBottles * numExchange
#     return ans
#
#
# print(numWaterBottles(5, 5))

# def searchInsert(nums, target):
#     if target <= nums[0]:
#         return 0
#     elif target > nums[-1]:
#         return len(nums)
#     else:
#         left_index = 0
#         right_index = len(nums) - 1
#         mid_index = int((left_index+right_index)/2)
#         while left_index + 1 < right_index:
#             if nums[mid_index] > target:
#                 right_index = mid_index
#                 mid_index = int((left_index + right_index) / 2)
#             elif nums[mid_index] < target:
#                 left_index = mid_index
#                 mid_index = int((left_index + right_index) / 2)
#             else:
#                 return mid_index
#         return mid_index + 1
#
#
# print(searchInsert([1,6], 6))

# def convertToTitle(columnNumber):
#     m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ans = []
#     while columnNumber > 26:
#         ans.append(m[columnNumber % 26 - 1])
#         if columnNumber % 26 == 0:
#             columnNumber -= 26
#         columnNumber = int(columnNumber/26)
#     ans.append(m[columnNumber-1])
#     return ''.join(ans[::-1])
#
#
# print(convertToTitle(2147483647))

# def maxProfit(prices):
#     m = prices[0]
#     profit = prices[0] - prices[0]
#     if len(prices) > 1:
#         for i in range(1, len(prices)):
#             m = min(m, prices[i-1])
#             if prices[i] - m > profit:
#                 profit = prices[i] - m
#     return profit
#
#
# print(maxProfit([2,4,1,10]))

# def titleToNumber(columnTitle):
#     m = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
#          'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
#          'Z': 26}
#     ans = 0
#     n = len(columnTitle)
#     for i in range(n):
#         ans += m[columnTitle[i]] * (26**(n-i-1))
#     return ans
#
#
# print(titleToNumber('AB'))

# def isIsomorphic(s: str, t: str):
#     ans1 = {}
#     ans2 = {}
#     for i in range(len(s)):
#         if s[i] not in ans1:
#             ans1[s[i]] = t[i]
#         else:
#             if ans1[s[i]] != t[i]:
#                 return False
#     for i in range(len(t)):
#         if t[i] not in ans2:
#             ans2[t[i]] = s[i]
#         else:
#             if ans2[t[i]] != s[i]:
#                 return False
#     return True
#
#
# print(isIsomorphic('qwer', 'ddgh'))

# def containsDuplicate(nums):
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             return True
#     return False
#
#
# print(containsDuplicate([1,2,2,3,4]))

# def findMinDifference(timePoints):
#     ans = []
#     for t in timePoints:
#         a = int(t[0])*10*60 + int(t[1])*60 + int(t[3])*10 + int(t[4])
#         ans.append(a)
#     ans.sort()
#     m = ans[0] - ans[-1] + 24*60
#     for i in range(1, len(ans)):
#         m = min(m, ans[i]-ans[i-1])
#         if m == 0:
#             return m
#     return m
#
#
# print(findMinDifference(["00:00", "23:59", "00:55"]))

# def containsNearbyDuplicate(nums, k):
#     ans = {}
#     for i in range(len(nums)):
#         if nums[i] not in ans:
#             ans[nums[i]] = i
#         else:
#             if abs(i - ans[nums[i]]) <= k:
#                 return True
#             else:
#                 ans[nums[i]] = i
#     return False
#
#
# print(containsNearbyDuplicate([1,2,3,1], 2))

# def isUgly(n: int):
#     while n > 1 and n % 2 == 0:
#         n /= 2
#     while n > 1 and n % 3 == 0:
#         n /= 3
#     while n > 1 and n % 5 == 0:
#         n /= 5
#     return n == 1
#
#
# print(isUgly(8))

# def missingNumber(nums):
#     n = len(nums)
#     return int((n+1)*n/2 - sum(nums))
#
#
# print(missingNumber([0, 1]))

# def isPowerOfFour(n: int):
#     while n > 1:
#         n /= 4
#     return n == 1
#
#
# print(isPowerOfFour(16))

# def countBits(n):
#     ans = []
#     for i in range(n + 1):
#         ans.append(bin(i)[2:].count('1'))
#     return ans
#
#
# print(countBits(30))

# def canWinNim(n):
#     return n % 4 != 0
#
#
# print(canWinNim(4))

# def canConstruct(ransomNote, magazine):
#     a, b = {}, {}
#     for r in ransomNote:
#         if r in a:
#             a[r] += 1
#         else:
#             a[r] = 1
#     for m in magazine:
#         if m in b:
#             b[m] += 1
#         else:
#             b[m] = 1
#     for r in a:
#         if r not in b:
#             return False
#         elif b[r] < a[r]:
#             return False
#     return True
#
#
# print(canConstruct('acdscs', 'csdcsacdsacds'))

# def moveZeroes(nums):
#     n = len(nums)
#     for i in range(n-1, -1, -1):
#         if nums[i] == 0:
#             nums.pop(i)
#             nums.append(0)
#     return nums
#
#
# print(moveZeroes([0,0,0]))

# def fizzBuzz(n):
#     ans = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             ans.append('FizzBuzz')
#         elif i % 3 == 0:
#             ans.append('Fizz')
#         elif i % 5 == 0:
#             ans.append('Buzz')
#         else:
#             ans.append(str(i))
#     return ans
#
#
# print(fizzBuzz(10))

# def distributeCandies(candyType):
#     n = int(len(candyType)/2)
#     ans = {}
#     for candy in candyType:
#         if candy in ans:
#             ans[candy] += 1
#         else:
#             ans[candy] = 1
#         if len(ans) >= n:
#             return n
#     if len(ans) >= n:
#         return n
#     else:
#         return len(ans)
#
#
# print(distributeCandies([1,1,1,1]))

# def fib(n):
#     a, b = 0, 1
#     i = 0
#     while i < n:
#         a, b = b, a+b
#         i += 1
#     return a
#
#
# print(fib(3))

# def hammingDistance(x, y):
#     a, b = list(bin(x)[2:]), list(bin(y)[2:])
#     ans = 0
#     n = min(len(a), len(b))
#     for i in range(-1, -n-1, -1):
#         if a[i] != b[i]:
#             ans += 1
#     if len(a) < len(b):
#         for i in range(len(b) - n):
#             if b[i] == '1':
#                 ans += 1
#     else:
#         for i in range(len(a) - n):
#             if a[i] == '1':
#                 ans += 1
#     return ans


# print(hammingDistance(12, 12))

# def findComplement(num):
#     ans = list(int(a) for a in bin(num)[2:])
#     ans_complement = list(map(lambda x: 1-x, ans))
#     a = 0
#     n = len(ans_complement)
#     for i in range(n):
#         a += ans_complement[i]*(2**(n - i - 1))
#     return a
#
#
# print(findComplement(1))

# def islandPerimeter(grid):
#     ans = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == 1:
#                 if j == 0 or grid[i][j-1] == 0:
#                     ans += 1
#                 if j == len(grid[i])-1 or grid[i][j+1] == 0:
#                     ans += 1
#                 if i == 0 or grid[i-1][j] == 0:
#                     ans += 1
#                 if i == len(grid)-1 or grid[i+1][j] == 0:
#                     ans += 1
#     return ans
#
#
# print(islandPerimeter([[1,1,0,1]]))

# def hammingWeight(n):
#     return bin(n)[2:].count('1')
#
#
# print(hammingWeight(21))
