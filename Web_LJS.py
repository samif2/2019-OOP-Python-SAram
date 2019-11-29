import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = None
'''
# chromedriver 의 위치를 path 에 저장한다
path = "chromedriver.exe"
# selenium 의 webdriver 로 크롬 브라우저를 실행한다
driver = webdriver.Chrome(path)
'''


def log_in(user_id, user_password, driver):
    '''
    :param user_id: 사용자의  달빛학사 아이디
    :param user_password:  사용자의 달빛학사 비밀번호
    :return: -
    '''

    # 사용자의 달빛학사 id와 비밀번호를 입력받는다
    # 달빛학사에 접속 - gmail 로 접속할지, id로 접속할지 입력받고 그에맞게 설정하지만, 아래는 우선 id-password 방법으로 로그인 하는 코드에요

    driver.get('https://go.sasa.hs.kr')
    time.sleep(1)
    driver.find_element_by_name('id').send_keys(user_id)
    time.sleep(1)
    driver.find_element_by_name('passwd').send_keys(user_password)
    driver.find_element_by_class_name('btn-info').click()
    time.sleep(2)


def is_free(target_name, time1):
    '''
    :param target_name:  찾고자 하는 사람의 이름 // main 에서 student_name
    :param time1:  찾고자 하는 날짜와 시간대 (ex. 월요일 5교시이면 1-5)
    :return: 공강이면 true, 수업이면 false를 반환
    '''
    # 타겟의 이름과 현재 시각을 x-y로 변환한 값을 입력받는다
    # 해당 시간에 타겟이 공강인지 판별하여 공강이면 'True'를 아니면 'False'를 return 한다
    # 공강시간검색 창으로 이동하여 사람의 이름을 입력한다
    # 동명이인인 김도현(3학년/1학년)에 대한 예외처리 필요

    time.sleep(2)
    driver.get('https://go.sasa.hs.kr/timetable/dup')
    # 타겟의 이름을 입력한다
    write_name = driver.find_element_by_class_name('form-control')
    time.sleep(1)
    write_name.send_keys(target_name)
    time.sleep(2)
    write_name.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    write_name.send_keys(Keys.ENTER)
    write_name.send_keys(Keys.ENTER)
    # 해당 시간에 공강인지 확인해준다
    titles = [
        element.text.strip()
        for element in driver.find_elements_by_id(time1)
    ]
    if not titles:
        return False
    else:
        # 공강이므로 True 를 return 한다
        return True

def import_timeteble(grade, time2, driver):
    '''
    :param grade:  찾고자 하는 사람의 학년 // main 에서 student_grade
    :param time2:  찾고자 하는 날짜와 시간대 (ex. 월요일 5교시이면 1-5)
    :return: 해당하는 시간대에 학년에 맞는 수업을 나열된 리스트를 반환합니다
    '''
    #  id 형식을 맞추어 새로운 변수인 table_time 에 저장합니다
    table_time = 'time'+time2

    if grade == 1:
        driver.get('https://go.sasa.hs.kr/timetable/search_new/all/1')
    else:
        driver.get('https://go.sasa.hs.kr/timetable/search_new/all/2')

    classes = [
        element.text.strip()
        for element in driver.find_elements_by_id(table_time)
    ]
    return classes
