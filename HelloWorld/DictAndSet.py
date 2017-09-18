"""
    dict:python内置字典，其他语言(java)成为map，使用键值对存储
    一个key对应一个value
    和list比较，dict有以下几个特点：
        查找和插入的速度极快，不会随着key的增加而变慢；
        需要占用大量的内存，内存浪费多。
        而list相反：

        查找和插入的时间随着元素的增加而增加；
        占用空间小，浪费内存很少。
        所以，dict是用空间来换取时间的一种方法。

    dict的key必须是不可变对象

    set:set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
        set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
        因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
"""
d = {"tom": 95, "jerry": 99, "lucy": 88}
v = d["tom"]
print(v)

# 想字典中添加值
d["groovy"] = 97
print(d)

# print(d["bob"])  # key不存在的时候会报错
# 避免key不存在时报错，有两种处理方式：1，取之前先使用in判断；2，通过dict提供的get()来取
if 'bob' in d:
    print(d['bob'])
else:
    print("没有bob")

vName = d.get('bob', -1)
print("dict的get()方法取值,没有要取的值就显示给的默认值(-1):", vName)

# 删除一个key使用pop(key)的方法
d.pop("groovy")
print("删除后的d：", d)

# set
s = set([1, 2, 2, 2, 3])

print("set去重:", s)

# set中添加值
s.add(10)
# set中移除值
s.remove(2)
