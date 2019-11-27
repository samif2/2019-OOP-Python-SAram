"""
사전에 만든 각종 파일을 import 해서 사용
Main 함수는 '사람을 찾는' 기능을 하는 함수이다.
Main 이전에 사용자의 id와 pw를 받아, 여러 번 id, pw 를 받을 필요가 없도록 한다.
"""

import SortingTime_LSI
import SortingTime_LSI
from main_Functions import *

print("Welcome! to our Program")
print("Made by 'Saram' in 2019")
print("=" * 20)
print("SASA 학생의 위치를 쉽게 찾아주는 프로그램입니다.")
print("=" * 20)


def Main():
    print("찾고자 하는 학생의 학년을 입력하세요.")
    student_grade = input('>')
    print("찾고자 하는 학생의 이름을 입력하세요.")
    student_name = input(">")

    # Web_LJS 실행
    # 만일 그런 사람이 없다면, 모든 과정을 생략하고 다시 할 것인지 묻는 부분으로 간다.

    # check_right_name = Wek_LJS
    # if check_right_name is True:

    print("찾고자 하는 날자를 입력하세요.")
    print("(입력 순서: 년도 월 일)")
    date = input('>')
    # 입력 처리 필요

    Question = "찾고자 하는 시간의 형식을 선택하세요"
    Menu_list = ["1. 교시 입력", "2. 시간(시 분) 입력"]
    Answer = Get_integer_Answer(Question, Menu_list, 2)

    Subject_list = []

    if Answer == 1:
        pass
    else:
        pass

    # Web 파일 중 공강인지 아닌지 알아봄
    # 공강이라면 (시간, 학년에 맞춰서) 도서관 혹은 공강실 등을 출력하고 종료 (return)

    Get_Answers_for_Student(Student_name=student_name, Subject_list=Subject_list)


check_Main = True
while check_Main is True:
    Main()
    Question_check = "다른 사람을 입력하겠습니까?"
    Answer_check = ["1. yes", "2. no"]
    check_Main = Get_integer_Answer(Question=Question_check, menu_list=Answer_check, range_num=2)
    if check_Main == 1:
        check_Main = True
    else:
        check_Main = False
