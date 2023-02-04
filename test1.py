lst = list(map(str, input().split()))
# # lst = input().split()
# print(round(sum(lst) / len(lst), 1))

cities = lst +["Москва", "Тверь", "Вологда"]

print(*cities)