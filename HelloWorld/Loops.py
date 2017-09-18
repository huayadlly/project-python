"""
    循环
    python中的循环有两种方式：for...in循环 和 while循环
"""

names = ["tom", "cat", "jerry"]
for name in names:
    print("for循环：", name)

# range()函数：可以生成一个整数序列，通过list()可以转换成list集合
numberList = list(range(10))  # 生成0-9的十个数，并放到list集合中
print("number list:", numberList)
numberSum = 0
for num in numberList:
    numberSum = numberSum + num
print(numberSum)

# 计算0 - 100的整数和
sum2 = 0
for number in list(range(100)):
    sum2 = sum2 + number
print(sum2)

# while循环：只要条件满足就不断循环
sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n
    n = n - 2
print("100内奇数的和：", sum3)

"""
    break: 在循环中可以提前退出循环
    continue: 在循环中结束当前循环，进入下次循环
"""
