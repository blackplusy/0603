#coding=utf-8

dic={'name':'gaga','age':18}
print(dic)
print(dic['name'])
print(dic['age'])

#修改字典
dic={'name':'heygor','qq':914338492}
print(dic)
dic['name']='葫芦娃'
print(dic)
dic['qq']=110
print(dic)

#删除字典
#del
dic={'name':'heygor','qq':914338492}
print(dic)
del dic['name']
print(dic)
del dic
#print(dic)
#clear
dic={'name':'heygor','qq':914338492}
print(dic)
dic.clear()
print(dic)
#keys
dic={'name':'heygor','qq':914338492}
print(dic.keys())
for i in dic.keys():
    print(i)
#values

dic={'name':'heygor','qq':914338492}
print(dic.values())
for i in dic.values():
    print(i)

#items
dic={'name':'heygor','qq':914338492}
for i,j in dic.items():
    print(i,j)











