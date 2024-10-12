a, b = map(int, input().split())
m = 0

#最大公约数
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        m = i
        break

print(f'{m} {int(a*b/m)}')