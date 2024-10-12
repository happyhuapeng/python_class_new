import re
s = input()
tmp = set(re.sub('[^A-Z]', '', s))
ans = sorted(tmp, key=s.index)
if ans:
    print(*ans, sep='')
else:
    print(f'Not Found')
