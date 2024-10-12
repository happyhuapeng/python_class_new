A, B = map(int, input().split())
i = A
Sum = 0
while i <= B:
    print(f'{i:>5d}', end='')
    Sum += i
    i += 1
    if (i - A) % 5 == 0 or i > B:
        print()
print(f'Sum = {Sum}')
