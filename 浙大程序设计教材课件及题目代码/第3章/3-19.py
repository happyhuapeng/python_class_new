n = int(input())
ans = ''

# 解法1
# StrLen = 0
# for _ in range(n):
#     s = input()
#     tmp = len(s)
#     if tmp > StrLen:
#         StrLen = tmp
#         ans = s

# 解法2
for _ in range(n):
    s = input()
    ans = max(ans, s, key=len)
print(f'The longest is: {ans}')
