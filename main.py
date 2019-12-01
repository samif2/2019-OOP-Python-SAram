"""
사전에 만든 각종 파일을 import 해서 사용
Main 함수는 '사람을 찾는' 기능을 하는 함수이다.
Main 이전에 사용자의 id와 pw를 받아, 여러 번 id, pw 를 받을 필요가 없도록 한다.
"""

import SortingTime_LSI
import control_command_LJH as cc
import basic_command_LJH as bc
from main_Functions import *

print("Welcome! to our Program")
print("Made by 'SAram' in 2019")
print("=" * 20)
print("SASA 학생의 위치를 쉽게 찾아주는 프로그램입니다.")
print("=" * 30)
print("help를 눌러 사용할 수 있는 명령어에 대해 알아보세요")
print("=" * 30)


def Main():

    print("찾고자 하는 날자를 입력하세요.")
    print("(입력 순서: 년도 월 일)")

    while True:
        date = input('>')
        date = date.split(' ')

        if len(date) != 3:
            print("잘못된 입력입니다.")

        try:
            date = list(map(int, date))
            date_year = date[0]
            date_month = date[1]
            date_day = date[2]
            break
        except:
            print("잘못된 입력입니다.")

    Question = "찾고자 하는 시간의 형식을 선택하세요"
    Menu_list = ["교시 입력", "시간(시 분) 입력"]
    Answer = Get_integer_Answer(Question, Menu_list)

    date_and_time = []
    if Answer == 1:
        print("교시를 입력하세요.")
        while True:
            Answer = input('>')

            try:
                Answer = int(Answer)
                if 1 <= Answer <= 12:
                    if Answer == 12:
                        Answer = 11
                    date_and_time = SortingTime_LSI.Sort_Time(year=date_year, month=date_month, day=date_day,
                                                              time_name=Answer)
                    break
                else:
                    print("잘못된 입력입니다.")
                    continue
            except:
                print("잘못된 입력입니다.")
                continue
    else:
        print("시 분 형식으로 원하는 시간을 입력해주세요.")
        print("24시간 형식을 따릅니다. (예시: 오후 11시 -> 23시)")
        while True:
            data_time = input('>')
            data_time = data_time.split(' ')

            if len(data_time) != 2:
                print("잘못된 입력입니다.")

            try:
                data_time = list(map(int, data_time))

                if data_time[0] < 0 or data_time[0] > 23:
                    print("잘못된 입력입니다.")
                    continue
                if data_time[1] < 0 or data_time[1] >= 60:
                    print("잘못된 입력입니다.")
                    continue

                time_hour = data_time[0]
                time_minute = data_time[1]
                date_and_time = SortingTime_LSI.Sort_Time(year=date_year, month=date_month, day=date_day,
                                                          hour=time_hour, minute=time_minute)
                break
            except:
                print("잘못된 입력입니다.")

    if date_and_time[0] == 6 or date_and_time[0] == 7:
        print("주말입니다. 기숙사에서 잘 찾아보세요... 화이팅!")
        return

    print("찾고자 하는 학생의 이름을 입력하세요.")
    student_name = input(">")

    ST = cc.Student(student_name)

    if type(ST.calender) == bool and not ST.calender:
        return

    q = ST.all_case(date_and_time[0], date_and_time[1])
    if q:
        print(q)
        Get_Answers_for_Student(Student=student_name, Subject_list=q)


bc.datalist = bc.load_info()

check_Main = True
bc.commandlist['Main'] = Main

while check_Main:
    command = input('>')
    try:
        bc.commandlist[command]()
    except KeyError:
        print(' 해당하는 명령어는 존재하지 않는 명령어 입니다. ')

    if command == 'Main':
        Question_check = "\n다른 사람을 입력하겠습니까?\n"
        Answer_check = ["yes", "no"]
        check_Main = Get_integer_Answer(Question=Question_check, menu_list=Answer_check)
        if check_Main == 1:
            check_Main = True
        else:
            check_Main = False
