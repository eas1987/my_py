print('2', 2, True, sep='|', end='-')

print(f'{b} {2} {3} TEST')              # форматная строка
print(r'E:\py_project\my_pytest.py')    # raw строка - игнорируются спец. символы


x, y = map(str, input('ввод нескольких значений через пробел ').split(sep=' '))
print(x, y)


numbers = [10, 15, 21, 33, 42, 55]
mapped_numbers = list(map(lambda elem: elem * 2 + 3, numbers))
print(mapped_numbers)