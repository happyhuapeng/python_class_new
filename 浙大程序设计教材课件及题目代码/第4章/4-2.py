cnt, ans = 0, 0


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


left, right = map(int, input().split())

for i in range(left, right + 1):
    if is_prime(i):
        cnt += 1
        ans += i
print(f'{cnt} {ans}')
