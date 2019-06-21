#coding=utf-8
a=(1)
print(a)
print(type(a))

a=(1,)
print(a)
print(type(a))

#访问元组

tup=(1,2,3,4)
print(tup)
for i in tup:
    print(i)

if 3 in tup:
    print('3 ishere')

#元组的索引和切片
tup=(1,2,3,4,5)
print(tup[0])
print(tup[-2])
print(tup[3:])
print(tup[:-3])

#删除元组
tup=(1,2,3)
del tup
#print(tup)

#补充
tup=(1,2,3,4,5,3,3)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(3))
print(tup.count(3))




