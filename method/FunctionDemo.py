# 计算绝对值函数
a = abs(-2)
print('绝对值：', a)

# 最大值
maxNumber = max(1, 2, 3, 8)
print('最大值是：', maxNumber)

# 数据类型转化
num = int(9.9)
print(num)  # num = 9,不是四舍五入

s = str(10.3)
print('字符串：', s)

print('Boolean值：', bool(1))
print('Boolean值：', bool(''))  # 非“1”既为false

# 可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print('给abs方法起别名：', a(-9))

n1 = 255
n2 = 1000
print('hex函数字符串化：', str(hex(n1)))
print('hex函数字符串化2：', str(hex(n2)))

"""
    自定义函数
    
    请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
    因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
    如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
"""


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print("自定义函数my_abs：", my_abs(-88))


# 定义一个空函数：pass -- 作为占位符,可以让代码先跑起来，避免报错
def my_nop(a1):
    if a1 > 18:
        pass


"""
    参数检查
"""


def my_abs_one(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if x > 0:
        return x
    else:
        return -x


print('增强：', my_abs_one(-9))
print('增强2：', my_abs_one(33))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 返回多个参数的时候，实际返回的是tuple
# 返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple
wx, wy = move(100, 100, 60, math.pi / 6)
print('计算移动坐标：', wx, wy)
w = move(120, 120, 60, math.pi / 6)
print('这次呢？:', w)

"""
练习

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax^2 + bx + c = 0
的两个解。
"""


def quadratic(aw, b, c):
    d = b * b - 4 * aw * c
    if d >= 0:
        d1 = math.sqrt(d)
        x1 = (-b + d1) / (2 * aw)
        x2 = (-b - d1) / (2 * aw)
        return x1, x2
    else:
        return


print("x^2 - 5x + 6 = 0的解为：", quadratic(1, -5, 6))
print("x^2 - 4x + 4 = 0的解为：", quadratic(1, -4, 24))
print("x^2 - 4x + 16 = 0的解为：", quadratic(2, 3, 1))
