# 本题要求统计一个整型序列中出现次数最多的整数及其出现次数。
#
# 输入格式：
# 输入在一行中给出序列中整数个数N（0<N≤1000），以及N个整数。数字间以空格分隔。
#
# 输出格式：
# 在一行中输出出现次数最多的整数及其出现次数，数字间以空格分隔。题目保证这样的数字是唯一的。

from collections import Counter

l = list(map(int, input().split()))
# 把N个整数，这个N踢掉
del l[0]
cnt = Counter(l)
print(*cnt.most_common(1)[0])

# ans = max(set(l), key=l.count)
# print(f'{ans} {l.count(ans)}')
