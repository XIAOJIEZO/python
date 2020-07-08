print("hello python world")

# 第一个注释
print('hello ,python!')

# \ 转义符  r去掉转义
print('转义,\n换行')
print(r'转义,\n换行')

# 等待用户输入
a = input('请输入，按回车结束：')
print('你输入的内容是：'+a)

# print输出默认换行，变量末尾加 end=""不换行
x = "a"
y = "b"
print(x)
print(y)

print(x, end="")
print(y)

"""
变量的命名和使用:
1、只能包含字母、数字和下划线
2、变量名不能包含空格，使用下划线分割单词
3、不要使用Python关键字和函数名用作变量名
4、变量名应既简短又具有描述性
"""

"""
字符串：字符串就是一系列字符，用引号括起的就是字符，可以是单引号，也可以是双引号，这种灵活可以在字符串中包含引号
"""
message = '去吧："皮卡丘"'
print(message)

# 使用方法修改字符串大小写
name = 'roger'
print(name.title())     # 首字母大写