n = int(input())
l = []
for _ in range(n):
    m = int(input())
    flag = 1
    for i in range(m):
        l = list(map(int, input().split()))
        for j in range(i):
            if l[j] != 0:
                flag = 0
                break
    if flag == 1:
        print('YES')
    else:
        print('NO')
