#coding=utf-8

#字符串的索引

name='baidu'

print(name[0])

print(name[-5])

print(name[4])

#字符串的切片

a='python'

print(a[4:])  #第5个字符到最后一个字符

print(a[:-4]) #直到倒数第四个字符之前

print(a[2:4]) #第三个字符到第四个字符

#字符串的拼接
a='python'
b=' is no.1'
print(a+b)
print(a+b[-1])

#遍历
for i in a:
    print(i)

#成员运算
if 't' in a:
    print('t is here!')

#去空格
str1='   python   '
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

#计算长度
str1='hello'
print(len(str1))

print('--------------')
#引号
print('python')
print("python")
print('''python''')

#print('i'm your baba!!!')

print("i'm your baba!!!")

print('i"m your mom!!')

'''
以下内容不会执行
别来了，没年终奖！
'''
print('''
name:'heygor'
age:18

''')




















