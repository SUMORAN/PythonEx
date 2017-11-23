#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

#第一句注释使得PY文件可以在LINUX或MAC的系统下直接运行文件
#保存源代码时要保存为UTF-8编码。第二句注释是为了告诉python解释器按照UTF-8编码读取
print('hello, my name is SuMo')
print('Age: %d, Sex: %s' % (21,'女'))
#如果只有一个%?，括号可以省略。
#用%%来表示一个%
print('\n')

print('1024 * 768 = ',1024*768)
print(r'\\\\\\\\\t\\\\')
#r表示原封不动输出引号内容
print('\n')
print('''line1
	line2
	line3''')
print('\n')

print(not 1<2)
print(5>3 or 1>3)
print('\n')
#None在Python中表示空值
#精确除：/   地板除：//   取余数：%

#Python使用Unicode编码
#ord()函数用来获取字符的整数表示
print('输出A的Unicode码值:',ord('A'))
print('输出中的Unicode值:',ord('中'))
#chr()函数把编码转化为对应的字符
print('直接写B的Unicode值以输出字母B:',chr(66))
#也可以直接写字符的Unicode编码值
print('直接写B的Unicode值以输出字母B:','\u4e2d\u6587')
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
ABC = 'ABC'.encode('ascii')
print("\'ABC\'.encode(\'ascii\')是：",ABC)
print("\'中文\'.encode(\'utf-8\')是：",'中文'.encode('utf-8'))
#！！！注意：纯英文的str可以用ASCII编码为bytes，内容是一样的，
#！！！含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，
#！！！因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#！！！在bytes中，无法显示为ASCII字符的字节，用\x##显示。

#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
#要把bytes变为str，就需要用decode()方法：
print("b'ABC'.decode('ascii')是：",b'ABC'.decode('ascii'))
#print("b'\xe4\xb8\xad\xe6\x96\x87'.decode('ascii')是：",b'\xe4\xb8\xad\xe6\x96\x87'.decode('ascii'))

print('\n')
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print("len('ABC'):",len('ABC'))
print("len(b'ABC'):",len(b'ABC'))
print("len('中文'):",len('中文'))
print("len('中文'.encode('utf-8')):",len('中文'.encode('utf-8')))
print('\n')

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('r = %.1f%%' %r)

#使用list和tuple
classmates = ['zhang','wang','li','hou']
print('classmates:',classmates)
num = len(classmates)
#空list长度为0
print('list中元素个数：',num)
#用索引来访问list中每一个位置的元素，记得索引是从0开始的
#当索引超出了范围时，Python会报一个IndexError错误
#所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素，以此类推，-2，,-3，-4
print('用索引输出元素：',classmates[0],classmates[-1])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('zhou')
classmates.append('xu')
#可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'liu')
#用pop()方法删除list末尾的元素
print('删除末尾元素：',classmates.pop())
#用pop(i)方法删除list第i位的元素
print('删除第i位元素：',classmates.pop(3))
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[2] = 'zhangliang'
print('classmates:',classmates)
#list中元素数据类型可以不同
L = ['zhangliang',707226025,'student','Wuhan university of techonogy',True]
print(L)
#list元素也可以是另一个list
M = ['person1:',L]
print(M)
print('M中元素个数：',len(M))
print(L[1],'     ',M[1][1])

#tuple一旦初始化就不能修改
tuple1 = (1,2,3,4)
tuple2 = (1,)
print(tuple1)
print(tuple2)
#“可变的”tuple,不改变tuple的元素，而改变tuple指向的list的元素
tuple3 = (1,2,[3,4])
print(tuple3)
tuple3[2][1] = 5
print(tuple3)

#条件判断
print('请输入你的年龄：')
age = input()
age = int(age)
if age >= 18:
	print('You have been an adult!')
elif age <= 12:
	print('You are still a child!')
else:
	print('You are a teenager!')
print('\n')


#循环
'''for student in classmates:
	print('Hello,',student)'''
#python提供一个range()函数
print(list(range(10)))
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
#while循环，求100以内奇数之和
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#使用dict和set
#Python内置了字典：dict的支持，dict全称dictionary，
#在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
#假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['A','B','C','D']
scores = [80,82,84,86]
#如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩
stu_score = {'A':80,'B':82,'C':84,'D':86}
print('B的成绩为：',stu_score['B'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
stu_score['C'] = 99
print('C的成绩为：',stu_score['C'])
#通过in判断key是否存在
print('E' in stu_score)
