def Get_integer_Answer(Question, menu_list, range_num):

    print(Question)

    for menu in menu_list:
        print(menu)
    while True:
        Answer = input('>')

        try:
            Answer = int(Answer)
        except:
            print("잘못된 입력입니다. 다시 입력하세요.")
            continue

        if 0 < Answer <= range_num:
            return Answer

        print("잘못된 입력입니다. 다시 입력하세요.")