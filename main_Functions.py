def Get_integer_Answer(Question, menu_list):
    """
    :param Question: 큰 질문. string 타입
    :param menu_list: 각각의 보기를 담고 있는 리스트.
    예시: ["먹기", "자기"]
    :return: 사용자가 답한 입력을 반환 (int 형)
    """
    print(Question)
    print("0을 누르면 이 질문을 취소합니다.")

    i = 1
    range_num = len(menu_list)
    for menu in menu_list:
        print(i, ": ", menu)
        i += 1

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


def Get_Class_info():
    print("반을 입력하세요.")
    while True:
        Answer = input('>')

        try:
            Answer = int(Answer)
        except:
            print("잘못된 입력입니다. 다시 입력하세요.")
            continue

        if 1 <= Answer <= 6:
            return Answer

        print("잘못된 입력입니다. 다시 입력하세요.")



def Get_Answers_for_Student(Student_name, Subject_list):
    print("=" * 20)
    print("학생 '" + Student_name + "' 찾는 중")
    Student_class = 0
    Student_sub = []

    while True:
        Question = "어떤 작업을 하시겠습니까?"
        Answers = ["추측한 모든 과목 보기", "반 정보 입력", "전공 및 부전공 입력", "듣지 않을 만한 수업 선택"]
        Answer = Get_integer_Answer(Question, Answers)

        if Answer == 0:
            print("학생 찾기를 종료합니다.")
            return

        print("-" * 20)
        if Answer == 1:

            print("가능성 있는 과목:")
            for Subject in Subject_list:
                print(Subject)
        elif Answer == 2:
            if Student_class != 0:
                Student_class = Get_Class_info()
            else:
                print("이미 정보를 가지고 있습니다.")
                print("반:", Student_class)
        elif Answer == 3:
            Question = "전공 및 부전공을 입력합니다."
            Answers = ["수학", "물리", "화학", "생명과학", "정보과학", "지구과학"]
            A = Get_integer_Answer(Question, Answers)
            if A == 6:
                A = 9
            else:
                A = -(A-1)
            Student_sub.append(A)
        elif Answer == 4:
            Question = "듣지 않을 만한 과목을 선택하세요."
            A = Get_integer_Answer(Question, Subject_list)
            del Subject_list[A-1]

        print("-" * 20)
