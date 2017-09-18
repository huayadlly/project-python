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


# 自定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print("自定义函数my_abs：", my_abs(-88))
