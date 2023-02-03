from builtins import print

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

print(my_string[1:5:1])                 # Срезы - Начало: Конец: Шаг
print(my_string * 5)                    # Дублирование строки
print(my_string.upper())                # Врег
print(my_string.lower())                # Нрег
print(my_string.replace('t', 'tt'))     # СтрЗаменить
print('strip', 'tttesttt'.strip('t'))   # СокрЛП. По умолчанию пробел, но можно любой символ
print('lstrip', '  test  '.lstrip())    # СокрЛ. По умолчанию пробел, но можно любой символ
print('rstrip', '  test  '.rstrip())    # СокрП. По умолчанию пробел, но можно любой символ


print(my_string.capitalize())           # С заглавной буквы
print('split', my_string.split(' '))    # Разложить строку в массив подстрок
print(my_string.count('t', 2, -1))      # Количество вхождений подсроки в строку
print('isalpha', my_string.isalpha())   # Только буквы в строке. Пробел НЕ буква
print('isdigit', '123456'.isdigit())    # Только цифры в строке.
print('rjust', '20'.rjust(5, '0'))      # Добавление лидирующих символов перед строкой
print('ljust', '21'.ljust(5, '0'))      # Аналогично rjust, но добавление символов в конец строки



print(my_string.find('t', 0, 7))        # Индекс первого вхождения. -1 если подстрока не найдена
print(my_string.rfind('t', 0, -1))      # Аналогично find, но поиск с конца
print(my_string.index('t', 0, -1))      # Аналогично find, но если плдстрока не найдена, будет вызвано исключение

str1 = '123456'
print(str1[-1::-1])                     # реверс строки с помощью среза

new_string = 'testrrtteettttt'
new_string = sorted(new_string)         # Сортировка
print('.'.join(['ab', 'pq', 'rs']))     # Конкатенация + вставка исходной строки между соединяемыми

