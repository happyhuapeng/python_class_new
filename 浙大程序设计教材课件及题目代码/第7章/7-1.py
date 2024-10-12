import re
import sys
from collections import Counter

s = sys.stdin.read()
s = str(re.sub(r'[^0-9a-zA-Z_]', ' ', s[:s.find("#")]))
new_l = list(map(str, s.replace('.', ' ').lower().split()))
for i in range(len(new_l)):
    if len(new_l[i]) > 15:
        new_l[i] = new_l[i][0:15]
new_l = sorted(new_l)`
print(len(set(new_l)))
d = list(Counter(new_l).most_common(len(set(new_l))))
for i in range(len(set(new_l)) // 10):
    print(f'{d[i][1]}:{d[i][0]}')
