# 比较简单 题解来源于网络
print('[1] apple')
print('[2] pear')
print('[3] orange')
print('[4] grape')
print('[0] exit')
lst = list(map(int, input().split()))
for i in range(0, 5):
    c = int(lst[i])
    if c == 1:
        print('price = 3.00')
    elif c == 2:
        print('price = 2.50')
    elif c == 3:
        print('price = 4.10')
    elif c == 4:
        print('price = 10.20')
    elif c == 0:
        break
    else:
        print('price = 0.00')

