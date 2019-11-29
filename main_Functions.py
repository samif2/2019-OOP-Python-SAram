Student_name = ""
Student_class = 0
Student_sub_list = []
Student_sub = []


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

        if 0 <= Answer <= range_num:
            return Answer

        print("잘못된 입력입니다. 다시 입력하세요.")


def Get_Class_info():
    global Student_class

    if Student_class != 0:
        print("이미 반 정보가 있습니다:", Student_class)

    print("반 정보를 입력하세요.")
    while True:
        Answer = input('>')
        try:
            Answer = int(Answer)
            if Answer == 0:
                print("이 작업을 취소합니다.")
                return Get_Answers_for_Student(Student_name, Student_sub_list)
            if 1 <= Answer <= 6:
                Student_class = Answer
                return Get_Answers_for_Student(Student_name, Student_sub_list)
        except:
            pass
        print("잘못된 입력입니다.")


def Quit_File():
    print("프로그램을 종료합니다.")
    return


def Print_all_Subject():
    print("모든 가능한 과목을 출력합니다.")

    for Sub in Student_sub_list:
        print(Sub)

    return Get_Answers_for_Student(Student_name, Student_sub_list)


def Get_Subject_info():
    global Student_sub

    Question = "전공 정보를 입력받습니다."
    Answers = ["수학", "물리", "화학", "생명과학", "정보과학", "지구과학"]
    Answer = Get_integer_Answer(Question, Answers)

    if Answer == 0:
        print("이 작업을 종료합니다.")
        return Get_Answers_for_Student(Student_name, Student_sub_list)

    Answer = -(Answer - 1)
    if Answer == -5:
        Answer = 9

    Student_sub.append(Answer)
    return Get_Answers_for_Student(Student_name, Student_sub_list)


def Get_Subject_info_no():
    global Student_sub_list
    Question = "듣지 않을 만한 과목을 선택하세요."
    Answer = Get_integer_Answer(Question, Student_sub_list)

    if Answer == 0:
        print("이 작업을 취소합니다.")
        return Get_Answers_for_Student(Student_name, Student_sub_list)
    del Student_sub_list[Answer-1]

    return Get_Answers_for_Student(Student_name, Student_sub_list)


def Print_Help():
    print("도움말을 출력합니다.")

    print("'quit': 프로그램을 종료합니다")
    print("'sll_sub': 가능한 모든 과목을 출력합니다.")
    print("'class_info': 학생의 반 정보를 입력합니다.")
    print("'subject': 전공, 혹은 부전공 과목을 입력합니다.")
    print("'no_sub': 듣지 않을 만한 과목을 입력합니다.")
    print("'help': 지금 보고있는 정보를 띄우는 명령어입니다.")


def Get_Answers_for_Student(Student, Subject_list):
    global Student_sub, Student_class, Student_name, Student_sub_list
    Student_name = Student
    Student_sub_list = Subject_list

    print("=" * 20)
    print("학생 '" + Student_name + "' 찾는 중")

    if len(Student_sub_list) <= 0:
        print("가능한 과목이 없습니다.")
        print("찾는 데에 실패했습니다.")
        print("프로그램을 종료합니다.")
        return

    Answers = {"quit": Quit_File, "all_sub": Print_all_Subject, "class_info": Get_Class_info,
               "subject": Get_Subject_info, "no_sub": Get_Subject_info_no, "help": Print_Help}

    print("어떤 작업을 하시겠습니까?")
    print("'help'를 입력하면 커맨드 도움말을 출력합니다.")

    while True:
        Answer = input('>')
        try:
            func = Answers[Answer]
            return func()
        except KeyError:
            print("잘못된 커맨드입니다.")