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
print("欢迎来到鱼虾蟹游戏！这是一个自动下注的版本，策略是每次都下同样大小的注，下在同一个图案")
print("骰子点数对应的图案如下：")
print("1:鱼 2:虾 3:瓢")
print("4:钱 5:蟹 6:鸡")

#计数
count_player_lose = 0
count_zhuang_lose = 0


balance = int(input("请输入玩家初始金额："))
zhuangjia = int(input("请输入庄家初始金额："))
bet_choice = int(input("请输入下注的图案编号（1~6）："))
count_range = int(input("请输入尝试次数："))
bet_amount = int(input("请输入每次下注的金额："))


for i in range (1,count_range):
    balance = 1000
    zhuangjia = 1000
    count_lose = 0
    while balance > 0 and zhuangjia > 0:
        
        if bet_amount > balance:
            bet_amount = balance


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
print("自动下注结束！")
print(f"玩家失败次数：{count_player_lose}")
print(f"庄家失败次数：{count_zhuang_lose}")