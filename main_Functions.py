import SubjectType_LSI
from time import sleep

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


def Quit_File():
    print("프로그램을 종료합니다.")
    return


def Print_all_Subject():
    print("모든 가능한 과목을 출력합니다.")

    for Sub in Student_sub_list:
        print(Sub)

    return Get_Answers_for_Student(Student_name, Student_sub_list)


def Use_Subject_info():
    global Student_sub_list

    print("입력받은 정보에 따라 과목을 재정렬합니다.")

    new_sub_list = []

    for sub_type in Student_sub:
        for sub in Student_sub_list:
            if sub_type == SubjectType_LSI.return_Subject_Type(sub):
                new_sub_list.append(sub)

    for sub in Student_sub_list:
        if sub not in new_sub_list:
            new_sub_list.append(sub)

    Student_sub_list = new_sub_list

    sleep(0.5)
    print("재정렬을 완료했습니다.")


def Get_Subject_info():
    global Student_sub

    Question = "전공 및 부전공 정보를 입력받습니다."
    Answers = ["수학", "물리", "화학", "생명과학", "정보과학", "지구과학"]
    Answer = Get_integer_Answer(Question, Answers)

    if Answer == 0:
        print("이 작업을 종료합니다.")
        return Get_Answers_for_Student(Student_name, Student_sub_list)

    Answer = -(Answer - 1)
    if Answer == -5:
        Answer = 9

    Student_sub.append(Answer)
    Use_Subject_info()
    return Get_Answers_for_Student(Student_name, Student_sub_list)


def Get_Subject_info_no():
    global Student_sub_list
    Question = "듣지 않을 만한 과목을 선택하세요."
    Answer = Get_integer_Answer(Question, Student_sub_list)

    if Answer == 0:
        print("이 작업을 취소합니다.")
        return Get_Answers_for_Student(Student_name, Student_sub_list)
    del Student_sub_list[Answer - 1]

    return Get_Answers_for_Student(Student_name, Student_sub_list)


def Print_Help():
    print("도움말을 출력합니다.")

    print("'quit': 프로그램을 종료합니다")
    print("'all_sub': 지금 듣고있을 가능성이 있는 모든 과목을 출력합니다.")
    # print("'class_info': 학생의 반 정보를 입력합니다.")
    print("'subject': 전공, 혹은 부전공 과목을 입력합니다.")
    print("'no_sub': 듣지 않을 만한 과목을 입력합니다.")
    print("'help': 지금 보고있는 정보를 띄우는 명령어입니다.")

    return Get_Answers_for_Student(Student_name, Student_sub_list)


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

    Answers = {"quit": Quit_File, "all_sub": Print_all_Subject,
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


if __name__ == '__main__':
    Get_Answers_for_Student('이소이', [1, 2, 3, 4, 5])
