#coding=utf-8
#直接访问
l=[1,2,3,4]
print(l)

#遍历访问
for i in l:
    print(i)

#成员运算符访问

if 4 in l:
    print('4 is here!')

#索引和切片

l=[1,2,3]
print(l)
print(l[0])
print(l[-2])
#print(l[3])

print(l[:-1])
print(l[1:])
print(l[1:2])

#列表的拼接
l1=[1,2,3]
l2=['a','b']
print(l1+l2)

#列表的更新
l=['kobe','james','cater']
print(l)
l[2]='rose'
print(l)
l=[1,2,[3,4],5]
print(l)
l[2][1]='a'
print(l)

#列表的删除
l=[3,4,5,6]
print(l)
del l[2]
print(l)





