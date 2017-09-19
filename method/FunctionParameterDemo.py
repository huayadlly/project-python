"""
    默认参数
注意：
    1.必选参数在前，默认参数在后，否则Python的解释器会报错
    2.如何设置默认参数
    3.当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
优点：
    默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现
"""


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print('5的平方：', power(5))


def enroll(name, gander, age=6, city='BeiJing'):
    print('name is:', name)
    print('gander is:', gander)
    print('age is:', age)
    print('city is:', city)
    print('--------')


enroll('Tom', 'boy')
enroll('Jerry', 'boy', 9)  # 顺序的方式给默认参数赋值，city没有赋值任然使用默认值
enroll('Lucy', 'girl', 8, 'London')
enroll('hyd', 'boy', city='Henan')  # 不按照顺序给默认参数赋值，需要指定参数的名字


# 默认参数必须指向不变对象！错误demo演示如下：
def wrong_demo(L=[]):
    L.append('END')
    return L


print(wrong_demo([1, 2, 3]))
print(wrong_demo())
print(wrong_demo())  # 开始出现错误：“ ['END', 'END'] ”


# 解决方法
def fix_demo(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print('---')
print(fix_demo())
print(fix_demo())

"""
    可变参数
1.可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
"""


def calc(number):
    c_sum = 0
    for item in number:
        c_sum = c_sum + item * item
    return c_sum


print('平方和：', calc([1, 2, 3]))  # 传入的参数是一个集合或者tuple


def calc(*numbers):
    s = []
    for i in numbers:
        s.append(i)
    print(s)
    # v = calc(s)
    return s


print('又是平方和？：', calc(1, 2, 3))
