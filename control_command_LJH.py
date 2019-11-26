import bs4
import requests
from selenium import webdriver
import time


class ControlTower:
    driver = None

    def __init__(self, driver=None):
        if driver is None:
            print("크롬드라이버는 필수사항입니다.")
            return

        self.driver = driver

    def get(self, url):
        return self.driver.get(url)

    def finding(self, element='id', inform=None, after='ret', sec=0, afterinform=None):
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

        func_list = {'id': self.driver.find_element_by_id,
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
        else:
            res.click()
            time.sleep(sec)


def Auto_Login(datalist):  # 파싱을 통해 창을 열지않고 로그인하여 접속
    pass

