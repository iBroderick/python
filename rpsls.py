#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈雄
日期：2020/11/19
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='石头':
        number=0
    elif name=='史波克':
        number=1
    elif name=='纸':
        number=2
    elif name=='蜥蜴':
        number=3
    elif name=='剪刀':
        number=4
    else :
        number=5
    return number

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        name='石头'
    elif number==1:
        name='史波克'
    elif number==2:
        name='纸'
    elif number==3:
        name='蜥蜴'
    else:
        name='剪刀'
    return name

def rpsls(player_choice_number):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    if player_choice_number == comp_number:
        print('您和电脑打平手了')
    else:
        if player_choice_number == 4:
            if comp_number == 2 or comp_number == 3:
                print('您赢了')
            else:
                print('计算机赢了')
        elif player_choice_number == 3:
            if comp_number == 2 or comp_number == 1:
                print('您赢了')
            else:
                print('计算机赢了')
        elif player_choice_number == 1:
            if comp_number == 0 or comp_number == 4:
                print('您赢了')
            else:
                print('计算机赢了')
        elif player_choice_number == 2:
            if comp_number == 1 or comp_number == 0:
                print('您赢了')
            else:
                print('计算机赢了')
        elif player_choice_number == 0:
            if comp_number == 4 or comp_number == 3:
                print('您赢了')
            else:
                print('计算机赢了')
        elif player_choice_number==5:
            print('Error:No Correct Name')
comp_number = random.randrange(0, 4)
    #产生随机数并赋给计算机
print("欢迎使用RPSLS游戏")
print('请输入您的选择：')
player_choice=input()
print("----------------")
    #将输入的字符转换
player_choice_number = name_to_number(player_choice)
comp_name = number_to_name(comp_number)
print('计算机的选择为：' + comp_name)
rpsls(player_choice_number)