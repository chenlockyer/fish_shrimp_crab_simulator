import random

# 定义骰子的点数和对应的动物
dice = {
    1: '鱼',
    2: '虾',
    3: '瓢',
    4: '钱',
    5: '蟹',
    6: '鸡'
}

# 玩家初始筹码


count_player_lose = 0
count_zhuang_lose = 0

for i in range (1,100):
    balance = 25
    zhuangjia = 25
    count_lose = 0
    while balance > 0 and zhuangjia > 0:

        # 玩家下注
        bet_amount = pow(2,count_lose)
        
        if bet_amount > balance:
            bet_amount = balance

        # 下注的动物
        bet_choice = 1
        # 骰子计数器初始化
        dic = {1:0,2:0,3:0,4:0,5:0,6:0}

        # 摇骰子
        dice_result1 = random.randint(1, 6)
        dice_result2 = random.randint(1, 6)
        dice_result3 = random.randint(1, 6)

        dic[dice_result1] += 1
        dic[dice_result2] += 1
        dic[dice_result3] += 1

        animal1 = dice[dice_result1]
        animal2 = dice[dice_result2]
        animal3 = dice[dice_result3]
        

        # 判断玩家是否赢得下注金额
        if dic[bet_choice] != 0:
            balance += bet_amount*dic[bet_choice]
            zhuangjia -= bet_amount*dic[bet_choice]
            count_lose = 0 
        else:
            balance -= bet_amount
            zhuangjia += bet_amount

            count_lose += 1 

    #判断谁破产
    if balance <= 0:
        print("游戏结束，你破产了！")
        count_player_lose += 1
    else:
        print("游戏结束，庄家破产了！")
        count_zhuang_lose += 1

#输出统计结果
print(f"玩家失败次数：{count_player_lose}")
print(f"庄家失败次数：{count_zhuang_lose}")