# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

"""
这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
"""

# 定义普通的tuple
classmates = ("tom", "cat", "Bob", "Jerry")

# 定义一个元素的tuple一个元素的tuple
t = (1,)
print("", t)  # 定义一个元素的tuple的时候需要加逗号，避免产生数学括号产生的歧义，显示的时候也会带上逗号，同样的道理

# 当tuple中的元素是list集合的时候，list的集合的元素三可以变化的，但是list指向的仍然是tuple的元素，这个三不变的
ee = ['A', 'B']
f = ('a', 'ｂ', ee)
ww = f[2][1]
print(ww)
ee = ['pp', 'kk']
f = ('a', 'ｂ', ee)
print(f[2][1])
