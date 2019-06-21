#coding=utf-8

l=[1,2,3,4]
print(l)
l.append('simida')
print(l)
l.append('omg')
print(l)

l.pop()
print(l)
l.pop()
print(l)

#获取列表的索引：元素在列表中第一次出现的位置
l=[1,2,3,4,3]
print(l.index(3))

l=['阿斯顿马丁','乔治巴顿','GTR',1]
print(l.index('乔治巴顿'))

for index,value in enumerate(l):
    print('索引是'+str(index)+' 的值是: '+str(value))

#列表的排序
print('-----------------------------------------')
l=[1,3,2,4]
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort()
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)

#列表推导式
#给定列表进行操作
a=[1,2,3,4]
print([3*x for x in a])
#没有给定列表可以使用range()方法
print([3*x for x in range(1,11)])
#加入if条件进行列表推导
print([x for x in a if x%2==0])
#多个for语句进行列表推到
print([[x,y] for x in range(2) for y in range(2)])











