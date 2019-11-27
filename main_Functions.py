def Get_integer_Answer(Question, menu_list, range_num):
    print(Question)
    print("0을 누르면 이 질문을 취소합니다.")

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
        elif Answer == 0:
            return False

        print("잘못된 입력입니다. 다시 입력하세요.")


def Get_Answers_for_Student(Subject_list):
    pass
