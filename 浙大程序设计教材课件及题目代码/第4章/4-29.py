l1 = list(input().split())
l1 = list(sorted(set(l1), key=l1.index))
del l1[0]
l2 = list(input().split())
l2 = list(sorted(set(l2), key=l2.index))
del l2[0]

ans = []

for i in l1:
    if i not in l2:
        ans.append(i)
for i in l2:
    if i not in l1:
        ans.append(i)

# 下面一行不加也可
ans = sorted(set(ans), key=ans.index)

print(*ans, sep=' ')
