N = int(input())

for i in range(2, N):
    if (i % 2 > 0 and i % 3 > 0) or i == 2 or i == 3:
        print(i, end=' ')