"""
사전에 만든 각종 파일을 import 해서 사용
Main 함수는 '사람을 찾는' 기능을 하는 함수이다.
Main 이전에 사용자의 id와 pw를 받아, 여러 번 id, pw 를 받을 필요가 없도록 한다.
"""

import SortingTime_LSI
import SortingTime_LSI

print("Welcome! to our Program")
print("Made by 'Saram' in 2019")
print("=" * 20)
print("SASA 학생의 위치를 쉽게 찾아주는 프로그램입니다.")
print("=" * 20)


def Main():
    print("찾고자 하는 학생의 이름을 입력하세요.")
    student_name = input(">")

    # Web_LJS 실행
    # 만일 그런 사람이 없다면, 모든 과정을 생략하고 다시 할 것인지 묻는 부분으로 간다.


check_Main = True
while check_Main is True:
    check_Main = Main()
