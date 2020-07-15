cards_list = []

def show_menu():
    print('*' * 50)
    print('欢迎使用【名片管理系统】 v1.0\n1. 新建名片\n2. 显示全部\n3. 查询名片\n\n0. 退出系统')
    print('*' * 50)

def build_cards():
    print('-' * 50)
    print('新建名片')
    print('-' * 50)

    name_str = input("请输入姓名: ")
    phone_str = input("请输入电话: ")
    email_str = input("请输入邮箱: ")
    qq_str = input("请输入qq: ")

    cards_dict = {"name" : name_str,
                  "phone" : phone_str,
                  "email" : email_str,
                  "qq" : qq_str}
    cards_list.append(cards_dict)
    print(cards_list)
    print("添加成功")

def show_all():
    if len(cards_list) == 0:
        print("请先添加数据")
        return

    print('-' * 50)
    print('显示全部')
    print('-' * 50)

    for key in ["姓名","电话","邮箱","qq"]:
        print(key,end="\t\t")
    print("")
    print("=" * 50)

    for card_list in cards_list:
        print('%s\t\t%s\t\t%s\t\t%s' % (card_list['name'],card_list["phone"],
                                  card_list['email'],card_list['qq']))

def search_cards():
    print('-' * 50)
    print('查询名片')
    print('-' * 50)

    find_name = input("请输入查找的姓名: ")

    for key in cards_list:
        if key['name'] == find_name:
           print('姓名\t\t电话\t\t邮箱\t\tqq\t\t')
           print('=' * 50)
           print('%s\t\t%s\t\t%s\t\t%s' % (key['name'], key["phone"],
                                           key['email'], key['qq']))
           deal_cards(key)
           break
        else:
            print('不存在')

def deal_cards(find_dict):
    print(find_dict)
    action = input('请选择操作: 1.修改  2.删除  0.返回上级 : ')
    if action == '1':
        find_dict['name'] = input_card_info(find_dict['name'],'名字：')
        find_dict['phone'] = input_card_info(find_dict['phone'],'电话：')
        find_dict['email'] = input_card_info(find_dict['email'],'邮箱：')
        find_dict['qq'] = input_card_info(find_dict['qq'],'qq：')
        print('修改名片成功')
    elif action == '2':
        cards_list.remove(find_dict)
        print('删除名片成功')


def input_card_info(dict_value,tip_message):
    return_str = input(tip_message)
    if len(return_str) > 0:
        return return_str
    else:
        return dict_value