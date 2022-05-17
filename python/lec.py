#print('hello word')

#Типы данных и переменные 
# int, float, boolean, str, list, None
# value = None



#a = 123
#b= 1.25
# print(type(a)) #type позволяет узнать тип данных 
#print(b)
#value = 1234
#print(value)
#s = 'Hello World'
#print(a,' - ', b, ' - ', s)
#print('{} - {} - {}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#list = [1,2,3,4] # '' в обозначении = список строк

#print(list)
 
# Ввод и вывод данных
#print('Введите а')
#a = int(input())
#print('Введите b')
#b = int(input())
#print(f'{a}, {b}')
#print(a, '+', b, '=',a+b)

# Арифметические операции 
# +, -, /, %, //, **,
# (), Сокращенные операции
#a = 2
#b = 8
#c=a-b
#print(c)

# Логические операции 
# >, >=, <, <=, ==, !-
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

#a = 1<3<5
#print(a)

# Управляющие конструкции 
# if, if-else

#a = int(input('a = '))
#b = int(input('b = '))
#if a>b:
    #print(a)
#else:
    #print(b)


#username = input('Введите имя: ')
#if username == 'Маша':
    #print('Ура, это же Маша!')
#elif username == 'Катя':
    #print('Я вас так ждал, Катя!')
#elif username == "Ильнар":
#    print('Ильнар - ТОП')
#else:
    #print('Привет,', username )

#original = 23
#inverted = 0
#while original !=0:
#    inverted = inverted * 10 + (original%10)
#    original //=10
#print(inverted)

# Управляющие конструкции
# for
#list = [1,2,3,4,5]
#for i in list:
#    print(i)

#r = range(10)
#for i in r:
#    print(i)

#for i in range(1,10,2):
#    print(i)

# ecsr

# text = 'Съешь ещё этих мягких французких булок'
# print(len(text)) #39
# print('ещё' in text) #True
# print(text.isdigit()) #False наличие цифр 
# print(text.islower()) #True - наличие нижнего регистра 
# print(text.replace('ещё', 'ЕЩЁ'))

# Списки 
# list = list

# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(numbers)
# for i in numbers:
#     i *=2
#     print(i)
# print(numbers)

# Функции 
def f(x):
    if x==1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 2.3
print(f(arg))
print(type(f(arg)))