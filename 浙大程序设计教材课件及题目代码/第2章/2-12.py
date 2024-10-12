a, b, c = map(int, input().split())

if 2 * max(a, b, c) >= a + b + c:
    print('These sides do not correspond to a valid triangle')
else:
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'area = {area:.2f}; perimeter = {perimeter:.2f}')
