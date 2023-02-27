myStr = input()
it = iter(myStr)
while True:
    elem = next(it)
    if elem == ' ':
        break
    else:
        print(elem, sep='', end='')
