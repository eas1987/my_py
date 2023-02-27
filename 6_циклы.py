
lst = list('test')
for index, value in enumerate(lst):           # Перебор пары "Индекс, Значение"
    print(index, value)


it = iter('test')                             # Итератор
elem = next(it, None)
while elem != None:
    print(elem)
    elem = next(it, None)







for i in range(5):                             # Диапазон
    print(i)