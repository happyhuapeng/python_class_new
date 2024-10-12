# 输入整数n（3<=n<=7）,编写程序输出1,2,...,n整数的全排列，按字典序输出。
#
# 输入格式:
# 一行输入正整数n。
#
# 输出格式:
# 按字典序输出1到n的全排列。每种排列占一行，数字间无空格。

def f(x,s=""):
	s+=x
	if len(s)<n:
		for i in num:
			if i not in s:
				f(i,s)
	else:
		print(s)
n=int(input())
num=[str(i+1) for i in range(n)]
for i in num:
	f(i)
