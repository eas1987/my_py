b = 'test'
print(f'{b} {2} {3} TEST')

print(len(b))               # Длина строки
print('st' in b)            # Вхождение строки в подстроку
print(ord('t'))             # Код символа

myText = '''
Способ ввода 
многострочного текста
!
'''
print(myText)

my_string = 'test string'

print(my_string * 5)                # Дублирование строки
print(my_string.capitalize())       # С заглавной буквы
print(my_string.split(' '))         # Разложить строку в массив подстрок
print(my_string[1:5:1])             # Срезы - Начало: Конец: Шаг

str1 = '123456'
print(str1[-1::-1])                 # реверс строки с помощью среза

new_string = 'testrrtteettttt'
new_string = sorted(new_string)     # Сортировка
print('.'.join(['ab', 'pq', 'rs'])) # Конкатенация + вставка исходной строки между соединяемыми
