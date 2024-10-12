# 输入一个字符串 str，再输入要删除字符 c，大小写不区分，将字符串 str 中出现的所有字符 c 删除。提示：去掉两端的空格。
#
# 输入格式:
# 在第一行中输入一行字符 在第二行输入待删除的字符
#
# 输出格式:
# 在一行中输出删除后的字符串
import re

s = input().strip()
chr = input().strip()

# 解法1
# ans = s.replace(c.upper(), "")
# ans = ans.replace(c.lower(), "")

# 解法2
c = '['+chr.lower()+chr.upper()+']'
ans = re.sub(c, "", s)

print(f'result: {ans}')