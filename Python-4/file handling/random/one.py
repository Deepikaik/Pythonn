import random

lotteryNum=[]
for x in range(10):
    lotteryNum.append(random.randint(102,200))

    luckydip=random.sample(lotteryNum,2)
    print(luckydip)