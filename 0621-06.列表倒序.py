#coding=utf-8
str1='abcd'
l=[]
l1=[]
for i in str1:
	l.append(i)
print(l)

b=len(l)
print(b)

for i in range(b):
        #print(i)
        #print(3-i)
        l1.append(l[3-i])

print(l1)
for i  in l1:
        print(i,end="")
