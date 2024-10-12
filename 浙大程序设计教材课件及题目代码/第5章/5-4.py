dic = {x: x for x in range(6, 11)}
x = list(map(int, input().split(',')))
x = set(list(filter(lambda i: i >= 6, x)))
for i in x:
    del dic[i]
print(*dic.values(), sep=" ")
