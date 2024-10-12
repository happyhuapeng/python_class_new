s, l = 0, 1

n = int(input())
for i in [i for i in range(n+1) if i % 2 ==1]:
    l = 1
    for j in range(1, i+1):
            l *= j
    s += l
print(f'n={n},s={s}')

