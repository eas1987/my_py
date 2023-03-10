lst1 = [1, 4, 2, 2, 3]

print(len(lst1))
print(min(lst1))
print(max(lst1))
print(sum(lst1))

print(sorted(lst1, reverse=True))           # Сортировка в новый список
lst1.sort()                                 # Сортировка текушего
# my_list.reverse()                         # Перевернуть список

lst2 = [6, 7, 8]

lst1.insert(0, -1)                          # Вставить значение
lst1.append(4)                              # Добавить
newList = lst1 + lst2                       # Сложение списокв в новый
lst1.extend(lst2)                           # Добавить список в текщий список

newList = newList*3                         # Дублирование элементв списка
print(6 in newList)                         # Проверка вхождения значения в список
del newList[4]                              # Удаление элемента по индексу
lst1.pop()                                  # Удалить элемент (по умолчанию последний)
lst1.remove(7)                              # Удалить первый найденный по значению
# my_list.clear()                           # Очистить список


newList2 = lst1.copy()                      # Создать новый список копированием
newList3 = lst1[:]                          # Создать новый список копированием с помоью среза
newList4 = list(lst1)                       # Создать новый список копированием с помоью метода

print('Кол-во четверок: ', lst1.count(4))   # Подсчитать количество значений
print('Индекс значения', lst1.index(4))     # Определить индекс значения
print('Количество элементов ', len(lst1))   # Количество элементов списка
print(lst1)

lst4 = list('t11t')
lst4[1:3] = ['e', 's']                      # Изменение элементов списка через срезы
lst4[1:3] = 'e', 's'
print(lst4)


# Сложение элементов вложенных списков
lst = [['1', '2', '5'],
       ['2', '1']
       ]
print(sum(lst, [])) # ['1', '2', '5', '2', '1']



# Генераторы списков (List comprehensions)
lstComp = [i for i in range(-5, 5) if i <= 0] # Генератор + условие
print('lstComp:', lstComp) # lstComp: [-5, -4, -3, -2, -1, 0]

myLst = [1, 3, 5, 2, 2, 4]
lstComp2 = ['чет' if val % 2 == 0 else 'нечет' for val in myLst] # Генератор + тернарный оператор условия
print('lstComp2: ', lstComp2)

