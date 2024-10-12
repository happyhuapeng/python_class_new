# 将一笔零钱换成5分、2分和1分的硬币，要求每种硬币至少有一枚，有几种不同的换法？
#
# 输入格式:
# 输入在一行中给出待换的零钱数额x∈(8,100)。
#
# 输出格式:
# 要求按5分、2分和1分硬币的数量依次从大到小的顺序，输出各种换法。每行输出一种换法，格式为：“fen5:5分硬币数量, fen2:2分硬币数量, fen1:1分硬币数量, total:硬币总数量”。最后一行输出“count = 换法个数”。
n = int(input())
count = 0
for i in range(n//5, 0, -1):
    for j in range(n//2, 0, -1):
        for k in range(n, 0, -1):
            if i*5 + j*2 + k == n:
                count += 1
                print(f'fen5:{i}, fen2:{j}, fen1:{k}, total:{i+j+k}')
print(f'count = {count}')
