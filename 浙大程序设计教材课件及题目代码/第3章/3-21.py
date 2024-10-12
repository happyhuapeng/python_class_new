s = input()
print(s)
tmp = ''.join(list(reversed(s)))
if s == tmp:
    print(f'Yes')
else:
    print(f'No')

# s = input()
# print(s)
# print('Yes' if s == s[::-1] else 'No')
# 1,2a2,1