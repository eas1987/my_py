a = b = c = 1
print(id(a), id(b), id(c))
print(type(a))

d, e = 1, 2
print(id(d), id(e)) # id объекта в памяти

d, e = e, d
print(d, e)

