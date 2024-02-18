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
balance = 1500
zhuangjia = 1000

print("欢迎来到鱼虾蟹游戏！")
print("骰子点数对应的图案如下：")
print("1:鱼 2:虾 3:葫芦")
print("4:铜钱 5:螃蟹 6:鸡")
print(f"当前金额为: {balance}")
print(f"庄家金额为{zhuangjia}")

while balance > 0 and zhuangjia > 0:


    # 玩家下注
    try:
        bet_amount = int(input("请输入下注金额: "))
        if bet_amount > balance:
            print("下注金额超过当前余额，请重新下注。")
            continue
        if bet_amount <= 0:
            print("下注金额须大于0，请重新下注。")
            continue
    except ValueError: #防止直接按enter键出现ValueError
        print("下注错误，请重新下注。")
        continue  

    # 玩家选择下注的动物
    try:
        bet_choice = int(input("请输入下注点数: "))
        if bet_choice not in [1,2,3,4,5,6]:
            print("下注错误，请重新下注。")
            continue
    except ValueError:
        print("下注错误，请重新下注。") 
        continue
    

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
    
    print(f"第一个骰子点数为 {dice_result1}，对应的图案为 {animal1}")
    print(f"第二个骰子点数为 {dice_result2}，对应的图案为 {animal2}")
    print(f"第三个骰子点数为 {dice_result3}，对应的图案为 {animal3}")

    # 判断玩家是否赢得下注金额
    if dic[bet_choice] != 0:
        balance += bet_amount*dic[bet_choice]
        zhuangjia -= bet_amount*dic[bet_choice]
        print(f"恭喜你赢得本局！收益为{bet_amount*dic[bet_choice]}")
        print(f"你的资产是{balance}")
        print(f"庄家的资产是{zhuangjia}")
    else:
        balance -= bet_amount
        zhuangjia += bet_amount
        print("很遗憾，本局你输了。")
        print(f"你的资产是{balance}")
        print(f"庄家的资产是{zhuangjia}")

#判断谁破产
if balance <= 0:
    print("游戏结束，你破产了！")
else:
    print("游戏结束，庄家破产了！")