from bs4 import BeautifulSoup as bs
import requests
import numpy as np
from selenium import webdriver
from basic_command_LJH import load_info
from SubjectType_LSI import *  # 학년 - 반정보 전용
import time, pickle, sys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")

database = load_info()

class ControlTower:  # control 을 구성하는 함수를 만들기위한 명령어들을 모아놓은 클래스
    driver = None

    def __init__(self, driver=None):
        if driver is None:
            print("크롬드라이버는 필수사항입니다.")
            return

        self.driver = driver

    def quit(self):
        self.driver.quit()

    def get(self, url):
        return self.driver.get(url)

    def url(self):
        return self.driver.current_url

    def finding(self, element='id', inform=None, after='ret', afterinform=None, sec=0):
        """
        일회용으로 정보생성에 편리하게 사용하기위해 find_element함수를 통합.
        부가 기능에 해당하는 time.sleep 함수까지 통합

        :param element: 사용할 정보의 종류 (id, name, xpath, c_name 네가지가 존재함.)
        :param inform: 사용할 정보
        :param after: find 이후 사용할 함수. 기본은 'ret'로 정보를 리턴함. (send, click이 부가로 존재)
        :param afterinform: 이후 사용할 함수에서 send 가 설정된 경우, 어떤 정보를 전달할지 정해줌.
        :param sec: 이후 time.sleep()를 통해 지연할 시간(초)
        :return: res 일때만 함수를 실행하지않은채로 객체를 리턴
        """

        func_list = {  # find 계열 함수들은 html 창에 있는 요소들을 가져옴
            'id': self.driver.find_element_by_id,
            'name': self.driver.find_element_by_name,
            'xpath': self.driver.find_element_by_xpath,
            'c_name': self.driver.find_element_by_class_name
         }

        res = func_list[element](inform)
        if after == 'ret':
            time.sleep(sec)
            return res

        elif after == 'send':
            res.send_keys(afterinform)
            time.sleep(sec)

        elif after == 'clear':
            res.clear()
            time.sleep(sec)

        else:
            res.click()
            time.sleep(sec)

    def auto_login(self, datalist):  # 자동으로 로그인하여 접속
        self.get('https://go.sasa.hs.kr')

        if datalist['logsys'] == 'sign_in':  # 달빛학사 로그인정보를 선택하는 경우
            self.finding('name', 'id', 'send', datalist['ID'], 1)  # ID 창에 사용자의 달빛학사 ID를 입력
            self.finding('name', 'Passwd', 'send', datalist['Password'], 1)  # PW 창에 사용자의 달빛학사 비밀번호를 입력
            self.finding('c_name', 'btn-info', 'click')  # sign in 버튼을 클릭
        else:
            self.finding('c_name', 'btn-flat', 'click', sec=1)  # ID 창에 사용자의 달빛학사 ID를 입력
            self.finding('name', 'identifier', 'send', datalist['gID'], 1)  # 사용자의 이메일 주소를 입력
            self.finding('c_name', 'CwaK9', 'click', sec=5)
            self.finding('c_name', 'whsOnd', 'send', datalist['gPassword'], 1)  # 사용자의 g-mail 비밀번호를 입력
            self.finding('c_name', 'CwaK9', 'click', sec=2)
        print(self.url())
        if str(self.url()) != 'https://go.sasa.hs.kr/main#':
            print("아이디나 비밀번호가 등록된 정보와 같지 않습니다. \n"
                  "프로그램을 재실행하여 아이디와 비밀번호를 다시 설정해 주세요.")
            self.quit()
            sys.exit(0)

    def souping_page(self):
        return bs(self.driver.page_source, 'html.parser')

##
class Student:
    CT = None
    calender = None; student_name = None
    student_grade = None; student_class = None
    student_sublist = None  # 수강할 만한 과목을 모두 모은 함수

    def __init__(self, st_name):
        '''
        :param st_name: 학생의 이름을 가져옴
        '''
        self.student_name = st_name
        self.CT = ControlTower(webdriver.Chrome('chromedriver.exe'))
        self.calender = self.importing_calender(st_name)
        pass

    def importing_calender(self, wanted):
        global database
        calenderbase = np.zeros((11, 7), dtype=bool)
        self.CT.auto_login(database)
        self.CT.get('https://go.sasa.hs.kr/timetable/dup')
        self.CT.finding('id', 'target', 'send', wanted, 1)

        soup = self.CT.souping_page()
        # Selenium 을 beautifulSoup에 이용하기위해 사용하는 과정
        founded_student = soup.select("#ui-id-1 li.ui-menu-item")

        if len(founded_student) == 0:
            print("해당하는 이름의 학생이 존재하지 않습니다")
            self.CT.quit()
            return False

        elif len(founded_student) > 1:
            for inform in founded_student:
                print(inform.find('div').getText())

            while True:
                number = int(input("%d 개의 자동완성이 있습니다. "
                                   "선택하고싶은 자동완성의 번호를 입력해주세요: " % (len(founded_student))))

                if number <= len(founded_student) or number > 0:
                    res_student = founded_student[number-1].find('div').getText()
                    self.student_grade = int(res_student[0])
                    self.student_class = int(res_student[2])
                    print(self.student_grade, self.student_class)
                    break
                print("입력정보가 잘못되었습니다. 다시출력해주세요")

        else:
            res_student = founded_student[0].find('div').getText()
            self.student_grade = int(res_student[0])
            self.student_class = int(res_student[2])
            print(self.student_grade, self.student_class)

        self.CT.finding('id', 'target', 'ret').clear()
        self.CT.finding('id', 'target', 'send', res_student, 1)
        self.CT.finding('c_name', 'btn-ms', 'click', 3)

        souping = self.CT.souping_page()
        time_schedule = souping.select("td.text-center")

        ###
        i = 0; q = 0
        for ping in time_schedule:
            if q == 0:
                q += 1
                continue

            if q == 8:
                i += 1
                q = 0
            if ping.find('span') is not None:
                calenderbase[i][q-1] = True
            else:
                calenderbase[i][q-1] = False
            q += 1

        print(calenderbase)

        '''
        for i in range(11):
            for q in range(9):
                if q == 0:
                    continue
                if time_schedule[i][q].find('span').getText() == ['공강']:
                    calenderbase[i][q] = True
                else:
                    calenderbase[i][q] = False

        print(calenderbase)
        '''
        return calenderbase

        # 모든 시간의 공강여부를 따져 배열에 저장한 뒤 반환하는 함수

    def import_timetable(self, grade, dayz, timez, ifemit = None):
        '''
        :param grade:  찾고자 하는 사람의 학년 // main 에서 student_grade
        :param time2:  찾고자 하는 날짜와 시간대 (ex. 월요일 5교시이면 1-5)
        :return: 해당하는 시간대에 학년에 맞는 수업을 나열된 리스트를 반환합니다
        '''
        #  id 형식을 맞추어 새로운 변수인 table_time 에 저장합니다
        table_time = 'time' + str(dayz) + '-' + str(timez)
        if ifemit is None:  # ifemit 에 무언가가 입력될경우, 사이트 변환하는 과정을 거치지 않는다.
            if grade == 1:
                self.CT.get('https://go.sasa.hs.kr/timetable/search_new/all/1')
            else:
                self.CT.get('https://go.sasa.hs.kr/timetable/search_new/all/2')

        classes = [
            element.text.strip()
            for element in self.CT.driver.find_elements_by_id(table_time)
        ]
        raw_table = classes[0].split('\n')
        time_table = list()

        for i in range(len(raw_table)):
            if 2 * i < len(raw_table):
                appart = raw_table[2 * i][: -1].split(' [')
                appart[1] = int(appart[1])
                #  과목의 이름만 한땀 한땀 가져오는데, 숫자와 과목을 구분짓는 ' [' 를 기준으로 split 시킨 리스트를 들여옴
                appart.append(raw_table[2*i+1].split(' / ')[1])
                # 그리고 그 다음원소가 담당 선생님, 강의실 이므로 강의실을 한 시간 단위에 해단하는 리스트에 추가한다.
                time_table.append(appart)
            else:
                break

        return time_table
    # 과목과 반, 강의실을 묶은 ( ex)  ['고급알고리즘' , 1, 'S401']) 리스트를 반환.

    def reject(self, time_table):
        # 학년, 필수과목의 반 정보처럼 다른 시간표의 탐색없이 과목정보만으로 미리 배제할 수 있는 정보를 배제한다.
        res_table = list()
        accepted_class = ['', [1], [0, 2], [0, 3]]
        # 1학년은 [1], 2학년은 2, 2와 3의 0, 3학년은 3, 2와 3의 0 이 입력될경우 수강 가능한것으로 처리한다.
        for timez in time_table:

            print(dict_Subject[timez[0]][0], accepted_class[self.student_grade])
            if dict_Subject[timez[0]][0] in accepted_class[self.student_grade]:
                # 해당 수업을 학생이 들을 수 없는 수업이라면(학년이 다른)
                res_table.append(timez)  # 해당 수업을 시간표 리스트에서 제외한다.

        return res_table

    def all_case(self, wanted_day, wanted_time):  # 원하는 날짜와 원하는 시간을 가져온다
        if self.calender[wanted_time-1][wanted_day-1]:
            print("공강시간입니다.공강실이나 도서관에 있을 확률이 높습니다.")
            return None
        # 공강시간이라면 공강이라고 알려줌

        prototype_table = self.import_timetable(self.student_grade, wanted_day, wanted_time)
        # 원하는 시간이 있다면 그 시간에 있을만한 모든 수업과 수업의 반, 강의실을 가져옴

        if self.student_grade == 1:
            for i in prototype_table:
                if i[1] == self.student_class:
                    return i  # 1학년은 전과목 필수이므로, 학생의 반은 수업의 반과 같다. 이를 이용하여 리턴한다.

        else:
            time_table = self.reject(prototype_table)
            # 일단 학생의 조건을 따라 몇가지 가능성들을 배제한다.

            for i in range(5):  # 모든 시간표를 돌아보며 공강 시간인데 중복되는게 있다면 뺀다.
                for q in range(11):
                    if [i+1, q+1] in [[wanted_day, wanted_time], [3, 5], [3, 6], [5, 5]]\
                            or (i == 4 and q > 6):
                        print("continuing")
                        continue
                    elif self.calender[q][i]:
                        extra_table = self.import_timetable(self.student_grade, i + 1, q + 1, 'emit')
                        for element in extra_table:
                            if element[0] == '소리예술':
                                continue
                            if element in time_table:
                                time_table.remove(element)
                                # 공강 시간표의 수업과 겹치는 수업이 있다면 배제한다.

            print(time_table)
            return time_table


if __name__ == '__main__':
    '''
    CT = ControlTower(webdriver.Chrome('chromedriver.exe'))
    CT.get('https://go.sasa.hs.kr')

    CT.finding(element='name', inform='id', after='send', afterinform='1897', sec=1)
    CT.finding(element='name', inform='passwd', after='send', afterinform='robin2001!', sec=1)
    CT.finding(element='c_name', inform='btn.info', after='click', sec=0)
    '''
    # ControlTower 사용예시
    ## 아이디 입력하고 1초 기다림 + 비밀번호 입력하고 1초 기다림 + 로그인

    name = input("이름을 입력해 주세요: ")
    ST = Student(name)
    q = ST.all_case(4, 7)

