from bs4 import BeautifulSoup as bs
import requests
import numpy as np
from selenium import webdriver
from basic_command_LJH import load_info
import time, pickle, sys


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
        :return: res 일떄만 함수를 실행하지않은채로 객체를 리턴
        """

        func_list = {'id': self.driver.find_element_by_id,  # find 계열 함수들은 html 창에 있는 요소들을 가져옴
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

        if datalist['logsys'] == 'sign_in':
            self.finding('name', 'id', 'send', datalist['ID'], 1)
            self.finding('name', 'Passwd', 'send', datalist['Password'], 1)
            self.finding('c_name', 'btn-info', 'click')
        else:
            self.finding('c_name', 'btn-flat', 'click', sec=1)
            self.finding('name', 'identifier', 'send', datalist['gID'], 1)
            self.finding('c_name', 'CwaK9', 'click', sec=5)
            self.finding('c_name', 'whsOnd', 'send', datalist['gPassword'], 1)
            self.finding('c_name', 'CwaK9', 'click', sec=2)
        print(self.url())
        if str(self.url()) != 'https://go.sasa.hs.kr/main#':
            print("아이디나 비밀번호가 등록된 정보와 같지 않습니다. \n"
                  "프로그램을 재실행하여 아이디와 비밀번호를 다시 설정해 주세요.")
            self.quit()
            sys.exit(0)


class Student:
    CT = None

    def __init__(self):
        self.CT = ControlTower(webdriver.Chrome('chromedriver.exe'))
        pass

    def importing_calender(self, wanted):
        global database
        calenderbase = np.zeros((11,7), dtype=bool)
        self.CT.auto_login(database)
        self.CT.get('https://go.sasa.hs.kr/timetable/dup')
        self.CT.finding('id', 'target', 'send', wanted, 1)

        source = self.CT.driver.page_source
        soup = bs(source, 'html.parser')
        # Selenium 을 beautifulSoup에 이용하기위해 사용하는 과정
        founded_student = soup.select("#ui-id-1 li.ui-menu-item")
        # 자동완성 리스트를 사이트에서 구해온다

        if len(founded_student) > 1:
            for inform in founded_student:
                print(inform.find('div').getText())

            while True:
                number = int(input("%d 개의 자동완성이 있습니다. "
                                   "선택하고싶은 자동완성의 번호를 입력해주세요: " % (len(founded_student))))

                if number <= len(founded_student) or number > 0:
                    res_student = founded_student[number-1].find('div').getText()
                    break
                print("입력정보가 잘못되었습니다. 다시출력해주세요")

        else:
            res_student = founded_student[0].find('div').getText()

        self.CT.finding('id', 'target', 'ret').clear()
        self.CT.finding('id', 'target', 'send', res_student, 1)
        self.CT.finding('c_name', 'btn-ms', 'click')
        time_schedule = soup.select("td.text-center")

        ###
        print(time_schedule.find('span').getText())
        for i in range(11):
            for q in range(9):
                if q == 0:
                    continue
                if time_schedule[i][q].find('span').getText() == ['공강']:
                    calenderbase[i][q] = True
                else:
                    calenderbase[i][q] = False

        print(calenderbase)
        pass
        ### 모든 시간의 공강여부를 따지는 프로그램, 전체적인 대 개편 수정 필요




if __name__ == '__main__':
    '''
    CT = ControlTower(webdriver.Chrome('chromedriver.exe'))
    CT.get('https://go.sasa.hs.kr')

    CT.finding(element='name', inform='id', after='send', afterinform='1897', sec=1)
    CT.finding(element='name', inform='passwd', after='send', afterinform='robin2001!', sec=1)
    CT.finding(element='c_name', inform='btn.info', after='click', sec=0)
    '''
    # ControlTower 사용예시
    # 아이디 입력하고 1초 기다림 + 비밀번호 입력하고 1초 기다림 + 로그인

    ST = Student()
    ST.importing_calender('권정준')
