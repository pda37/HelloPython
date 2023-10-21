import math

print("hello,world")
import keyword
print(keyword.kwlist)
age=20
if age>20:
    print(age)
else:
    print(20)
s='hello python lemon'
print(s[1::2])
print(s[::2])
print(s[18::-1])
print(s[13:18])
new_s=s[1::2]
print(new_s)
print(type(s))
print(len(s))

def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

a=2.06
b=2.05
print(a%b)
a=int(input('年龄：'))
if a>=18:
    print('已成年')
else:
    print('未成年')

name=str(input('用户名：'))
pwd=str(input('密码：'))
user_1={name:pwd}
print(user_1.keys())
user={'hu':'123456','zhang':'111111','li':'222222'}
if user_1.keys() in user.keys():
    print('允许登录')
else:
    print('禁止登录')

a=int(input('请输入a的值：'))
b=int(input('请输入b的值：'))
c=int(input('请输入c的值：'))
if a>0:
    if b>0:
        if c<0:
            print('业务处理2')
            print('流程结束')
        else:
            print('业务处理3')
            print('流程结束')
    else:
        print('业务处理2')
        print('流程结束')
else:
    print('业务处理1')
    if c<0:
        print('业务处理2')
        print('流程结束')
    else:
        print('业务处理3')
        print('流程结束')

year=int(input('输入年份：'))
if (year%4==0 and year%100!=0) or year%400==0:
    print('{}是闰年'.format(year))
else:
    print('{}是平年'.format(year))

num=int(input('请输入一个五位数：'))
if num>=10000 and num<=99999:
    a=int(num/10000)
    b=int((num-10000*a)/1000)
    c=int((num-10000*a-1000*b)/100)
    d=int((num-10000*a-1000*b-100*c)/10)
    e=num%10
    # print(a,b,c,d,e)
    if a==e and b==d:
        print('{}是回文数'.format(num))
    else:
        print('{}不是回文数'.format(num))
else:
    print('该数不是五位数')

import random
num=random.randint(1,9)
a=int(input('输入一个数字：'))
if a>num:
    print('bigger')
elif a<num:
    print('less')
elif a==num:
    print('equal')

sum=0
i=1
a=int(input('1到a的求和,a='))
while i<=a:
    sum=sum+i
    i+=1
print(sum)

n=10
count=0
while n>0:
    sex=input('性别：')
    if sex=='f':
        age=int(input('年龄：'))
        if age>=10 and age<=12:
            print('该女生可以加入球队')
            count+=1
        else:
            print('该女生不满足年龄限制')
    else:
        print('仅限女生')
    n-=1
print('满足条件可加入球队的有{}人'.format(count))

# 石头剪刀布的游戏
import random
roles = ['曹操', '张飞', '刘备']
mora = ['剪刀', '石头', '布']
a = int(input('选择角色，请输入1-3，1曹操,2张飞,3刘备：'))
print('你选择了{}'.format(roles[a-1]))
sum_win = 0
sum_loss = 0
sum_draw = 0
while True:
    b = int(input('请出拳，请输入1-3，1剪刀，2石头，3布：'))
    print('你选择了{}'.format(mora[b-1]))
    robot = random.randint(1, 3)
    print('机器人出了{}'.format(mora[robot-1]))
    if b == robot:
        print('平局')
        sum_draw += 1
    elif b-robot == -1 or b-robot == 2:
        print('机器人胜')
        sum_loss += 1
    elif b-robot == 1 or b-robot == -2:
        print('{}胜'.format(roles[b-1]))
        sum_win += 1
    choice = input('是否继续，请输入y/n：')
    if choice == 'y':
        continue
    else:
        break
print('本次对局你赢了{}次，输了{}次，平局{}次'.format(sum_win, sum_loss, sum_draw))

# 猜数游戏
import random
num = random.randint(1, 1000)
print("我的数字是{}".format(num))
a = int(input("猜一个数："))
while True:
    if a > num:
        print("数太大了")
        a = int(input("继续猜："))
        continue
    elif a < num:
        print("数太小了")
        a = int(input("继续猜："))
        continue
    elif a ==num:
        print("猜对了！")
        b = input("是否继续，yes/no：")
        if b == "yes":
            print("我的数字是{}".format(num))
            print(num)
            a = int(input("猜一个数："))
            continue
        else:
            break

str_1 = input("输入字符串：")
n = len(str_1)
str_2 = str_1[-1:-n-1:-1]
str_3 = str_1[::-1]
print(str_1)
print(str_2)
print(str_3)

def mySqrt(x):
    j = int((len(str(x)) - 1)/2)
    i = 10**j - 1
    while i <= x:
        if i * i < x:
            i = i + 1
        elif i * i > x:
            return i - 1
        else:
            return i


# x 的平方根
def mySqrt(x):
    a = 0
    b = x
    c = int((a + b + 1)/2)
    while a != c:
        if c**2 == x:
            break
        elif c**2 > x:
            b = c
            c = int((a + b)/2)
        else:
            a = c
            c = int((a + b) / 2)
    return c


r = mySqrt(1000)
print(r)


# 两数之和
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 整数反转
class Solution:
    def reverse(self, num):
        if num == 0:
            return 0
        # elif num > (2**31-1) or num < -2**31:
        #     return 0
        else:
            dig = list(str(d) for d in str(num))  # 整数拆分成列表
            if num > 0:
                dig.reverse()
                num02 = int(''.join(dig))  # 将列表连接成字符串并转换成整数
                if num02 > (2**31-1):
                    return 0
                else:
                    return num02
            else:
                del dig[0]
                dig.reverse()
                num02 = int(''.join(dig))
                num03 = num02*(-1)
                if num03 < -2**31:
                    return 0
                else:
                    return num03


# 罗马数字转整数
class Solution:
    def romanToInt(self, roman):
        roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a = 0
        for i in range(0, len(roman)-1):
            if roman_int[roman[i]] >= roman_int[roman[i+1]]:
                a = a + roman_int[roman[i]]
            else:
                a = a - roman_int[roman[i]]
        a = a + roman_int[roman[-1]]
        return a


# 盛最多水的容器
class Solution:
    def maxArea(self, height):
        a = 0
        i = 0
        j = len(height)-1
        while i < j:
            s = abs((i-j)*(min(height[i], height[j])))
            a = max(a, s)
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return a

# 表示该类是从哪个类继承而来的，所有类最终都会继承自 object 类
class Solution(object):
    """
    关于特殊方法 __init__
    方法__init__() 是一个特殊的方法，用于对对象进行初始化，每当根据类创建新实例时，Python都会自动运行它
    每个方法第一个参数都是 self，指向实例本身，也就是说它们是和实例绑定的函数，这也是我们称它们为方法而不是函数的原因
    """
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_num_add(self):
        for i in range(len(self.nums)-1):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]


# 类对象支持两种操作：属性引用和实例化
result = Solution([3, 2, 4, 100, 1000, 10000], 11000)  # 实例化
result.two_num_add()  # 属性引用

def isValid(s):
    if s == '':
        return False
    else:
        if (len(s) % 2) != 0:
            return False
        else:
            dic = {'(': -1, ')': 1, '{': -2, '}': 2, '[': -3, ']': 3}
            list_s = list(str(d) for d in s)
            while list_s:
                if dic[list_s[0]] + dic[list_s[-1]] == 0 and dic[list_s[0]] < dic[list_s[-1]]:
                    list_s.pop(0)
                    print(list_s)
                    list_s.pop()
                    print(list_s)
                elif dic[list_s[0]] + dic[list_s[1]] == 0 and dic[list_s[0]] < dic[list_s[-1]]:
                    list_s.pop(0)
                    print(list_s)
                    list_s.pop(0)
                    print(list_s)
                else:
                    break
            if not list_s:
                return True
            else:
                return False


print(isValid("(([]){})"))

def plusOne(digits):
    a = 0
    for i in range(len(digits)):
        a += digits[i] * (10**(len(digits)-1-i))
    a += 1
    dig = list(int(d) for d in str(a))
    return dig

def longestCommonPrefix(self, strs) -> str:
    if len(strs) == 1:
        return strs[0]
    else:
        b = 0
        short = len(strs[0])
        for i in range(len(strs)-1):
            short = min(short, len(strs[i+1]))
        if short == 0:
            return ''
        else:
            for j in range(short):
                a = 1
                for m in range(len(strs)-1):
                    if strs[m][j] == strs[m+1][j]:
                        a += 1
                if a == len(strs):
                    b += 1
                else:
                    break
            return strs[0][0:b]

def isValid(s):
    if s == '':
        return False
    else:
        # while s != '':
        #     if '()' in s:
        #         s = s.replace('()', '')
        #     elif '{}' in s:
        #         s = s.replace('{}', '')
        #     elif '[]' in s:
        #         s = s.replace('[]', '')
        #     else:
        #         break
        # return s == ''
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


print(isValid(""))

class Solustion:
    """
    爬楼梯，n阶楼梯，每次只能爬1或2阶，有多少种不同的方法可以爬到楼顶
    假设爬n阶楼梯的方法有 f(n) 种
    最后一步只有爬1或2阶两种情况
    如果最后一步爬1阶，则爬n阶楼梯的方法有 f(n-1) 种
    如果最后一步爬2阶，则爬n阶楼梯的方法有 f(n-2) 种
    即 f(n)=f(n-1)+f(n-2)
    从 n=1 推算
    f(1)=1
    f(2)=2
    f(3)=f(2)+f(1)
    f(4)=f(3)+f(2)
    f(5)=f(4)+f(3)
    ...
    f(n)是一个累加的过程，即斐波那契数列
    """
    def __init__(self, n):
        self.n = n

    def climbStairs(self):
        li = [1, 2]
        i = 2
        while i < self.n:
            li.append(li[i-1]+li[i-2])
            i += 1
        print(li)
        return li[self.n-1]


r = Solustion(10)
print(r.climbStairs())

def constructRectangle(self, area: int):
    b = int(math.sqrt(area))
    while b > 0:
        a = int(area / b)
        if area % b == 0 and a >= b:
            break
        else:
            b -= 1
    return [a, int(area / a)]

def addBinary(a, b):
    la = list(int(c) for c in a)
    la.reverse()
    lb = list(int(d) for d in b)
    lb.reverse()
    long = max(len(a), len(b))
    lc = []
    x = 0
    for i in range(long):
        if la[i] + lb[i] + x < 2:
            lc.append(la[i] + lb[i] + x)
            la.append(0)
            lb.append(0)
            x = 0
        else:
            lc.append(la[i] + lb[i] - 2 + x)
            la.append(0)
            lb.append(0)
            x = 1
    if x == 1:
        lc.append(1)
    lc.reverse()
    s1 = [str(m) for m in lc]
    s2 = ''.join(s1)
    return s2


print(addBinary('10001', '0111111111'))

def lengthOfLastWord(s):
    s1 = s.strip()
    a = 0
    for i in range(len(s1), 0, -1):
        if s1[i-1] == ' ':
            break
        else:
            a += 1
    return a


print(lengthOfLastWord("   fly me   to   the moon  "))

def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    else:
        a, b = 1, 1
        for i in range(len(s)):
            if b == 26:
                break
            else:
                print(s)
                for j in range(i+1, len(s)):
                    if s[j] in s[i:j]:
                        break
                    else:
                        a += 1
            b = max(a, b)
            a = 1
        return b


def lengthOfLongestSubstring(s):
    st = {}
    i, ans = -1, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i)
        st[s[j]] = j
        print(st, i, ans)
    return ans


print(lengthOfLongestSubstring("dvdfdzxcn"))

import operator
from functools import reduce


def singleNumber(nums):
    num = 0
    for i in nums:
        num = operator.xor(num, i)
    # num = reduce(operator.__xor__, nums)
    return num


print(singleNumber([4, 1, 2, 1, 2, 6, 4]))

def strStr(haystack, needle):
    return haystack.find(needle)


print(strStr("", ""))

def merge(nums1, m, nums2, n):
    for i in range(len(nums1)-1, m-1, -1):
        nums1.pop(i)
    nums1.extend(nums2)
    nums1.sort()
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

def wordPattern(pattern, s):
    pl = list(str(a) for a in pattern)
    sl = s.split(' ')
    if len(pl) != len(sl):
        return False
    else:
        li = []
        for i in range(len(pattern)):
            li.append({pattern[i]: sl[i]})
        print(pl, sl, li)
        if pl.count(pl[0]) == len(pl):
            return sl.count(sl[0]) == len(sl) and len(pl) == len(sl)
        elif pl == pl[::-1]:
            if sl.count(sl[0]) == len(sl):
                return False
            elif sl == sl[::-1]:
                for j in range(int(len(pl)/2)):
                    if pl.count(pl[j]) != sl.count(sl[j]):
                        return False
            return sl == sl[::-1] and sl.count(sl[0]) != len(sl)
        elif pl == sl[::-1] or pl == sl:
            return True
        else:
            for j in range(len(li) - 1):
                for k in range(j + 1, len(li)):
                    if str(li[j].keys()) == str(li[k].keys()):
                        if str(li[j].values()) != str(li[k].values()):
                            return False
                    elif str(li[j].values()) == str(li[k].values()):
                        if str(li[j].keys()) != str(li[k].keys()):
                            return False
            return True

def wordPattern(pattern, s):
    pl = list(str(a) for a in pattern)
    sl = s.split(' ')
    li = []
    for i in range(len(pattern)):
        li.append({pattern[i]: sl[i]})
    print(li)
    for j in range(len(li)-1):
        for k in range(j+1, len(li)):
            if str(li[j].keys()) == str(li[k].keys()):
                if str(li[j].values()) != str(li[k].values()):
                    return False
    return True


print(wordPattern("jquery", "jquery"))

def findPoisonedDuration(timeSeries, duration):
    if len(timeSeries) == 1:
        return duration
    else:
        time = 0
        for i in range(len(timeSeries) - 1):
            time += min((timeSeries[i + 1] - timeSeries[i]), duration)
        time += duration
        return time


print(findPoisonedDuration([1, 20], 10))

def largestTriangleArea(points):
    s_max = 0
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                # a = points[i][0]
                # b = points[i][1]
                # c = points[j][0]
                # d = points[j][1]
                # e = points[k][0]
                # f = points[k][1]
                s = abs(points[i][0] * points[j][1] + points[i][1] * points[k][0] + points[j][0] * points[k][1] - points[i][0] * points[k][1] - points[i][1] * points[j][0] - points[j][1] * points[k][0]) / 2
                s_max = max(s_max, s)
    return s_max


print(largestTriangleArea([[8, 3], [5, 3], [7, 7], [0, 10]]))

def superPow(a, b):
    c = [1] * len(b)
    ans = 1
    for i in range(len(b)):
        c[i] = a ** b[i]
        for j in range(len(b)-i-1):
            c[i] = ((c[i] % 1337)**10) % 1337
    c[-1] = c[-1] % 1337
    for k in range(len(c)):
        ans *= c[k]
    return ans % 1337


print(superPow(a=2147483647, b=[2, 0, 0]))

def grayCode(n):
    ans = []
    for i in range(2**n):
        print(i ^ i)
        ans.append(i ^ (i >> 1))

    return ans


print(grayCode(4))

def reverseBits(n):
    lis = list(int(a) for a in str(n))
    print(lis)
    lis.reverse()
    print(lis)
    ans = 0
    for i in range(len(lis)-1, -1, -1):
        print(i)
        ans += lis[i]*(2**i)
    return ans


print(reverseBits(100111111111111111111111111111101))

def isPowerOfTwo(n):
    if n == 1:
        return True
    else:
        while n > 1:
            if n % 2 == 1:
                return False
            n /= 2
        return n == 1


print(isPowerOfTwo(8))

def findJudge(n, trust):
    if n > len(trust) + 1:
        return -1
    else:
        ans = []
        for i in range(1, n + 1):
            ans.append(i)
        for j in range(len(trust)):
            if trust[j][0] in ans:
                ans.remove(trust[j][0])
        print(ans)
        for a in ans:
            m = 0
            for k in range(len(trust)):
                if trust[k][1] == a:
                    m += 1
            if m == n-1:
                return a
        return -1


print(findJudge(4, [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]))

def canPermutePalindrome(s):
    lis = []
    ans = 0
    for b in s:
        if b not in lis:
            if s.count(b) % 2 != 0:
                ans += 1
            lis.append(b)
    return ans <= 1


print(canPermutePalindrome('tatooa'))

def addDigits(num):
    while num > 9:
        ans = 0
        for n in str(num):
            ans += int(n)
        num = ans
    return num


print(addDigits(38))

# 走楼梯的方法，一次可以走1或2或3阶，思路同一次走1或2阶楼梯
def waysToStep(n):
    # ans = [1, 2, 4]
    # if n > 3:
    #     for i in range(3, n):
    #         ans.append(ans[i-1]+ans[i-2]+ans[i-3])
    # print(ans)
    # return ans[n-1] % 1000000007  752119970
    a, b, c = 1, 2, 4
    i = 1
    while i < n:
        a, b, c = b % 1000000007, c % 1000000007, (a + b + c) % 1000000007
        i += 1
    return a % 1000000007


print(waysToStep(61))

def thirdMax(nums):
    nums.sort(reverse=True)
    print(nums)
    a, b, c = nums[0], nums[0], nums[0]
    for i in range(len(nums)):
        if nums[i] == a:
            continue
        else:
            b = nums[i]
            for j in range(i, len(nums)):
                if nums[j] == b:
                    continue
                else:
                    c = nums[j]
                    break
            break
    print(a, b, c)
    return c


print(thirdMax([1,2,2,5,3,5]))

def convertToBase7(num):
    ans = []
    n = abs(num)
    while n >= 7:
        a = n % 7
        n = int(n / 7)
        ans.insert(0, str(a))
    ans.insert(0, str(n))
    h = ''.join(ans)
    if num >= 0:
        return h
    else:
        return '-' + h


print(convertToBase7(-7))

def toHex(num: int):
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    ans = []
    if num < 0:
        n = 2**32 - abs(num)
    else:
        n = num
    while n >= 16:
        a = n % 16
        n = int(n / 16)
        ans.insert(0, d[a])
    ans.insert(0, d[n])
    h = ''.join(ans)
    return h


print(toHex(26))

def threeSumClosest(nums, target):
    ans = nums[0] + nums[1] + nums[2]
    dif = abs(ans - target)
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if abs((nums[i] + nums[j] + nums[k]) - target) < dif:
                    ans = nums[i] + nums[j] + nums[k]
                    dif = abs(nums[i] + nums[j] + nums[k] - target)
                if dif == 0:
                    return ans
    return ans


print(threeSumClosest([-1,2,1,-4], 1))

def permute(nums):
    """ 全排列 :param nums 输入 nums = [1,2,3] :return: 输出[ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]] """
    # 保存满足条件的解
    # 第1步：定义结果集变量
    res = []
    nums_len = len(nums)

    # 第2步：定义回溯方法
    def backtrack(visitedItems, leftNums):
        """visitedItems: 已遍历的元素
        leftNums:剩下的数组(待遍历的数组) """
        if len(visitedItems) == nums_len:
            # 当遍历的元素数目等于输入nums的数组长度时，寻找到解，添加到res数组
            res.append(visitedItems)
            # 递归出口，【注意：递归的结束一定 要有return】
            # 没看懂这个 return
            return
        # 递归回溯方法backtrack
        for i in range(len(leftNums)):
            """ visitedItems+[leftNums[i]]:已遍历的数组追加
            leftNums[:i] + leftNums[i+1:]：表示剩余的数组，即除掉当前的元素 """
            backtrack(visitedItems+[leftNums[i]], leftNums[:i] + leftNums[i+1:])
    # 调用内部回溯算法
    backtrack([], nums)
    # 返回结果集
    return res


print(permute([1, 2, 3]))

def maxProfit(prices):
    m = prices[0]
    profit = prices[0] - m
    if len(prices) > 1:
        for i in range(1, len(prices)):
            m = min(m, prices[i])
            if prices[i] - m > profit:
                profit = prices[i] - m
    return profit


print(maxProfit([7,6,4,3,1]))

def majorityElement(nums):
    ans = {}
    for num in nums:
        if num not in ans:
            ans[num] = 1
        else:
            ans[num] += 1
    print(ans, ans.items())
    a = sorted(ans.items(), key=lambda an: an[1], reverse=True)
    return a[0][0]


print(majorityElement([1,1,2,3,4,4,5,5,5,5]))

def reverseBits(n: int):
    a = bin(n)[2:]
    ans = '0' * (32 - len(a)) + a
    return int(ans[::-1], 2)


print(reverseBits(1010010100011110100))

