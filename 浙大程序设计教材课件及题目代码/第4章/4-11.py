def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, x//2+1):
            if x % i == 0:
                return False
    return True


for _ in range(int(input())):
    n = int(input())
    print('Yes' if is_prime(n) else 'No')

