count = int(input('кол - во элементов '))
new_list = []
for i in range(1, count + 1):
    # in_val = 'новый элемент ' + str(i) + ': '
    # el = input(in_val)
    el = input(f'new el # {i}: ')
    new_list.append(el)

print(new_list)

b = 'test'
print(f'{b} {2} {3} TEST')