# Файлы # Хранение данных # Передача данных в клиент-серверных проектах
# Хранение конфигов # Логирование действий
# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') #открыли файл
# data.writeline(colors) # произвели запись (разделителей не будет
# data.close() # обязательно закрыть(разорвать связь) иначе нельзя будет потом удолить или будет утечка памяти


# path = 'fail.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()

# with open('file.txt', 'w') as data: #закрытие файла будет автоматически
#     data.write('line 1\n')
#     data.write('line 2\n')
#                                           ФУНКЦИИ


# def f(x):
#     if x == 1:
#        return 'Целое'
#     elif x == 2.3:
#        return 23
#     else:
#         return

# import hello
# print(hello.f(1))

# def new_string(symbol, count):# функция распознает тип данных в момент вывода 
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # ошибка: TypeError missing 1 required ...
# print(new_string(4)) # 12

# def concatenatio(*params):
#  res: str = "" #указываем тип данных потому что хотим работоть со строкой 
#  res = 0 #работаем с числами int, указывать тип не обязательно
#  for item in params:
#  res += item
#  return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2

#                                          РЕКУРСИЯ 
# (функция вызывающая сама себя, главное при описании рекурсии указать в какой момент нужно остановиться и перестать её вызывать)
# 
#                      КОРТЕЖ это неизменяемый список
# (a) = (3, 4)
# print(a)
# print(a[0]) # обращение к конкретному элементу или (a[-1])
#  #кортеж с циклом:
# (a) = (3, 4, 8, 96)
# for item in a:
#     print(item)

# # t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t # двойное преобразование, распоковываем кортеж и работаем с отдельными переменными
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

 #   СЛОВАРИ  Неупорядоченные коллекции произвольныхобъектов с доступом по ключу

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# for k in dictionary.keys(): # для показа ключей
# for k in dictionary.values(): #для показа значений
#     print(k)

# МНОЖЕСТВА:  Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set
# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

#неизменяемые множества
# s = frozenset(a)
# или
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

#            СПИСКИ
list1 = [1,2,3,4,5]
list2 = list1
for e in list1:
    print(e)
print()
for e in list2:
    print(e)
-----------
list1[0] = 123 #значение мняется и в 1 и во 2 списке
for e in list1:
    print(e)
print()
list2[1] = 333 #значение мняется и в 1 и во 2 списке
for e in list2:
    print(e)
#удаление последнего элемента списка
list1 = [1,2,3,4,5]
print(list1.pop())
print(len(list1))# выводим сколько элементов будет в листе
print(list1.pop(2)) # сразу удаляем нужный элемент 
print(list1.insert(2, 11))  #[2]- это индекс, 11 новый элемент между 2 и 3  вставить на нужную позицию элемент
 print(list1.append(11))  #добавление в конец нового элемента 11