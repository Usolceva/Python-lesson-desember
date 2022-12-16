#print(type(a))
#print(type(b))

a = 123
b = 1.123
s = 'hello world'
print(s) # вывод строки
print('hello "world') #вывод с 2-й ковычкой
print("hello 'world") #вывод с одинарной ковычкой
s = 'hello \'world' #вывод одинарной ковычки
s = 'hello \nworld' #вывод на строку ниже слова world
print(a, b, s) #вывод переменных в одну строку поочереди
print(a, '_',b, '_', s) #с пробелами
print('{} - {} - {}'.format(a, b, s)) #вывод переменных 
print('{1} - {2} - {0}'.format(a, b, s)) #a=0, b=1, s=2 вывод переменных непопорядку
print(f'{a} - {b} - {s}') #вывод переменных(интерполяция)более удобен

f = True  #Логическая переменная
k = False #Логическая переменная
print(f, k)

#массив в сшарпе = список в питоне
list = []
list = [1, 2, 3] #массив чисел
list = ['1', '2', '3', 'hello'] # массив строк
print(list)

#запрос от пользвателя:
print('ВВедите a');
a = input() #для вывода строк
print('введите b');
b = input()
print(a, ' + ', b, ' = ', a+b)
# для вывода чисел нужо перед input писать тип данных(int, float...)
print('ВВедите a');
a = int(input()) #для вывода строк
print('введите b');
b = int(input())
print(a, ' + ', b, ' = ', a+b)

#арифметические операции
a = 123
b = 321
c = a+b
print(c)

a = 123
b = -321 #унарный минус
c = a+b
print(c)

a = +123 #унарный плюс но обычно он не пишется
b = 321
c = a+b
print(c)

a = 123
b = 321
c = a / b #один слеш это деление  вещественных чисел
print(c)

c = a // b #деление в целых числах, ответ без запятой
c = a % b # остаток от деления
c= a ** b #возведение в степень

a = 1.3
b = 3
c = round(a * b, 3) #round: для выщитывания вещественных чисел если не писать то число в ответе будет округленое, 3 после запятой - количество цифр после запятой в ответе

#сокращенные операции присваивания
a = 3
a += 5 #(-=, *=, /= и тд..)
print(a)

#логические операции >, >=,<, <=, ==, !=; not, and, or, не путать с &, |, ^; is, is not, not in; gen
a = 1 > 4
print(a)

a = 1 < 4 and 5 > 2
print(a)

a = 1 < 3 < 5 #можно использовать тройные неравенства
a = 1 < 3 < 5 < 10 #или даже четверные
print(a)

f = 1
t = 4
x = 123
print(f<t>(x))

a = 1 == 2 #операция сравнения
print(a)

a = 1 != 4 #операция неравества
print(a)

a = 'hello'
b = 'hello'
print(a == b) #сравние сторк

a = [1,2]
b = [1,2]
print(a == b) #сравниене списков

f = 1 > 2 or 4 < 6 # или (получаем правда, потому что-то одно из высказываний истина)

a = [1,2,3,4]
print(2 in a) #спрашиваем есть двойка в списке или нет
print(not 2 in a) #говорим что двойки в списке или нет и получаем ответ фолсе потому что 2 есть

is_odd = f[0] % 2 == 0 # остаток от деления на 2 у числа с индексом 0, ответ фолсе так как 1 нечетное число
#ноль это лож а единица это истина
is_odd = not f[0] % 2
print(is_odd)

# управляющие конструкции if, if-else

a = int(input('a ='))
b = int(input('b =')) 
if a > b:
    print(a)
else:
    print(b)

name = input('введите имя:')
if name == 'Маша':
    print('Ура Маша')
elif name =='Марина':
    print('Ура Марина')
elif name =='Ильнар':  
    print('Ильна топ')
else:
    print('Привет, ', name)

# циклы while, for
original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит)')
print(inverted)

for i in 1,2,3,4,5:
    print(i**2)

r = range(10)
for i in r:
    print(i)

for i in range(1, 10, 2)# пробежаться от 1 до 10, по нечетным цифрам, 1, 3,5 и тд..

#строки
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#списки введение
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
ran = range(1, 6)
print(type(ran))
numbers = list(ran) #приведение типа range к типу list
print(type(numbers))

print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len') # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2 #в текущую переменну кладем новое значение не в сам список
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

#расщиренные функции

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

#функции
def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

def f(x):
 if x == 1:
     return 'Целое'
 elif x == 2.3:
      return 23
 else:
       return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType



