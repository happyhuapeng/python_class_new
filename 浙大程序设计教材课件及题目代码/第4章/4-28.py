l = list(map(int, input().split()))
for i in range(3):
    for j in range(3):
        print(f'{l[j*3+i]:>4d}', end='')
    print()
