# 随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。 如没有10个英文字母，显示信息“not found”
#
# 输入格式:
# 在一行中输入字符串
#
# 输出格式:
# 在一行中输出最左边的10个不重复的英文字母或显示信息“not found"

ans = ''
for i in input():
    if i.isalpha() and i.upper() not in ans and i.lower() not in ans:
        ans += i
        if len(ans) == 10:
            print(f'{ans}')
            break
else:
    print(f'not found')
