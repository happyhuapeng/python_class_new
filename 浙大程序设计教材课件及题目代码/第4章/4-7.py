n = int(input())

if n == 0:
    average, count = 0, 0
else:
    l = list(map(int, input().split()))
    average = sum(l) / len(l)
    count = len([x for x in l if x >= 60])

print(f'average = {average:.1f}')
print(f'count = {count}')

