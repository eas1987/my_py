my_list = [1, 2, 3]

my_list.insert(0, -1)           # Вставить

my_list.append(4)               # Добавить
my_list.append(4)

my_list[-1] = 5                 # Обратиться к последнему элементу

new_list = [6, 7, 8]
my_list.extend(new_list)        # Добавить список

my_list.sort()  #
# my_list.reverse()             # Перевернуть список

my_list.pop()                   # Удалить элемент (по умолчанию последний)

my_list.remove(7)               # Удалить первый найденный

# my_list.clear()

print('Кол-во четверок: ', my_list.count(4))
print('Количество элементов ', len(my_list))
print(my_list)

print('ТестоваяСтрока'[1: 5: 1])  # - Начало: Конец: Шаг

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
