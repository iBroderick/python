#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2020/11/19
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=='ʯͷ':
        number=0
    elif name=='ʷ����':
        number=1
    elif name=='ֽ':
        number=2
    elif name=='����':
        number=3
    elif name=='����':
        number=4
    else :
        number=5
    return number

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        name='ʯͷ'
    elif number==1:
        name='ʷ����'
    elif number==2:
        name='ֽ'
    elif number==3:
        name='����'
    else:
        name='����'
    return name

def rpsls(player_choice_number):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    if player_choice_number == comp_number:
        print('���͵��Դ�ƽ����')
    else:
        if player_choice_number == 4:
            if comp_number == 2 or comp_number == 3:
                print('��Ӯ��')
            else:
                print('�����Ӯ��')
        elif player_choice_number == 3:
            if comp_number == 2 or comp_number == 1:
                print('��Ӯ��')
            else:
                print('�����Ӯ��')
        elif player_choice_number == 1:
            if comp_number == 0 or comp_number == 4:
                print('��Ӯ��')
            else:
                print('�����Ӯ��')
        elif player_choice_number == 2:
            if comp_number == 1 or comp_number == 0:
                print('��Ӯ��')
            else:
                print('�����Ӯ��')
        elif player_choice_number == 0:
            if comp_number == 4 or comp_number == 3:
                print('��Ӯ��')
            else:
                print('�����Ӯ��')
        elif player_choice_number==5:
            print('Error:No Correct Name')
comp_number = random.randrange(0, 4)
    #��������������������
print("��ӭʹ��RPSLS��Ϸ")
print('����������ѡ��')
player_choice=input()
print("----------------")
    #��������ַ�ת��
player_choice_number = name_to_number(player_choice)
comp_name = number_to_name(comp_number)
print('�������ѡ��Ϊ��' + comp_name)
rpsls(player_choice_number)