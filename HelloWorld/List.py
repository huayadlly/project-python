# list是python内置的一种有序集合
classmate = ["tom", "cat", "Bob", "Jerry"]
print(classmate)

# 获取集合的长度
length = len(classmate)
print("集合的长度：", length)

# 获取集合中的元素，索引从0开始
name1 = classmate[1]
print("第一个元素：", name1)

# 也可以从后往前去元素: 如果索引的长度大于元素的个数，回报异常：IndexError错误
name = classmate[length - 1]
print("最后一个元素：", name)
name4 = classmate[-1]
print("也是最后一个元素：", name4)

# 指定位置插入元素
classmate.insert(4, "my_new")

# 要删除指定位置的元素的时候，需要使用pop(i)方法，其中i表示的是索引的位置：
# classmate.pop(1)   # 删除第二个位置上的元素
# print("删除后的集合：", classmate)
# 删除末尾的元素使用pop() 方法

# list的元素也可以是list集合
s = ["java", "php", "python"]
v = ['google', 'baidu', s, 'taobao']
# 其中php的表示方式可以是v[2][1], 也可以是s[1]
php1 = v[2][1]
php2 = s[1]
print("两种不同的表示方式： ", php1, php2)
if php1 == php2:
    print("两则相等吗？：", "true")

# 如果集合中一个元素也没有，表示集合为空，长度为0
L = []
print("空集合的长度为：", len(L))
