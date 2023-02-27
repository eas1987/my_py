N = int(input())
lst = []
for i in range(N):
    curLst = []
    for j in range(N):
        if j == N - 1:
            curLst.append(5)
        else:
            curLst.append(1)
    lst.append(curLst)

# for i in range(0, N):
#     lst[i][N-1] = 5

for i in range(N):
    print(*lst[i])