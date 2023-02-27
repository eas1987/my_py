s = '+7(xxx)xxx-xx-xx'
n = input().rjust(len(s))
for i, item in enumerate(n):
    if s[i] == item or s[i] == 'x' and item.isdigit():
        continue
    print('НЕТ')
    break
else:
    print('ДА')