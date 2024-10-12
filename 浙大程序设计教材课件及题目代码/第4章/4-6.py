import sys

n = int(input())
a, b = 1, 1
if n < 1:
    print(f'Invalid.')
    sys.exit()
else:
    for i in range(n):
        print(f'{a:>11d}', end='')
        a, b = b, a+b
        if i % 5 == 4:
            print()
