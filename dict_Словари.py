
# текст в формате json
new_dict = {'key1': 'value 1', 'key2': 'value 2', 'key3': 'value 3'}
# new_dict = dict(key1='value 1', key2='value 2')

# print(new_dict['key1333']) - ошибка
# print(new_dict.get('key1333')) - None

if new_dict.get('key1333') == None:
    print('key not found')

# new_dict.pop('key1')

print(new_dict.items())
print(new_dict.keys())
print(new_dict.values())

for key, value in new_dict.items():
    print(f'{key} - {value}')



