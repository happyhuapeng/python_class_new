m, n = map(int, input().split())
flag = 0
for i in range(m, n+1):
    l = []
    for j in range(1, int(i**0.5)+1):
        if i % j == 0 and j != 1:
            l.append(j)
            l.append(i//j)
    if sum(l) == i-1:
        flag = 1
        l.sort()
        print(f'{i} = 1 + ', end='')
        print(*l, sep=' + ')
if flag == 0:
    print(f'None')