import cards_tool
while True:
    cards_tool.show_menu()
    action_str = input("请选择希望执行的操作： ")
    print('你的操作为: 【%s】' % action_str)

    if action_str in ['1','2','3']:
        if action_str == '1':
            cards_tool.build_cards()
        elif action_str == '2':
            cards_tool.show_all()
        elif action_str == '3':
            cards_tool.search_cards()
    elif action_str == "0":
        print('欢迎您下次再用')
        break
        pass
    else:
        print('输入不正确,请重新输入')