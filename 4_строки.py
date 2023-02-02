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
print(my_string[1:5:1])             # - Начало: Конец: Шаг

new_string = 'testrrtteettttt'
new_string = sorted(new_string)
print(''.join(new_string))
