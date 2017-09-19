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
enroll('Jerry', 'boy', 9)
enroll('Lucy', 'girl', 8, 'London')
