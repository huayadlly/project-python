"""
    条件判断

    1. if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
"""
age = 60
if age >= 50:
    print("老年人，age:", age)
    print("your age is:", age)
elif age > 18:
    print("成年人：", age)
    print("your age is :", age)
else:
    print("年轻人：", age)
    print("your age is :", age)

# 只要x是非零数值，非空字符串，非空list时，就判断为true,否则为false
x = 3
if x:
    print("True~")

# input()方法中输入后接收到的数据是str类型的，需要使用int()方法转换成int类型后才能和int类型的数据比较
s = input("Input Your Birthday:")
s = int(s)
if s < 2000:
    print("00前")
else:
    print("00后")
