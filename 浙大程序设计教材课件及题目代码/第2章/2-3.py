# 为了提倡居民节约用电，某省电力公司执行“阶梯电价”，安装一户一表的居民用户电价分为两个“阶梯”：月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；超过50千瓦时的，超出部分的用电量，电价上调0.05元/千瓦时。请编写程序计算电费。
#
# 输入格式:
# 输入在一行中给出某用户的月用电量（单位：千瓦时）。
#
# 输出格式:
# 在一行中输出该用户应支付的电费（元），结果保留两位小数，格式如：“cost = 应付电费值”；若用电量小于0，则输出"Invalid Value!"。

InputNumber = float(input())

result = 0
price = 0.53

if 0 <= InputNumber <= 50:
    result = price*InputNumber
elif InputNumber > 50:
    result = (price+0.05)*(InputNumber-50)
    result += 50 * price

if InputNumber < 0:
    print('Invalid Value!')
else:
    print('cost = %.2f' % result)
