l = list(map(int, input().split(',')))
n = int(input())
flag = 0
# 练习一下filter，可以不加这行
l = list(filter(lambda x: x < n, l))
for i in range(len(l)):
    if n - l[i] in l:
        print(f'{i} {l.index(n - l[i])}')
        flag = 1
        break
if not flag:
    print(f'no answer')

