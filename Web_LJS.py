import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def log_in(user_id, user_password):

    # chromedriver의 위치를 path에 저장한다
    path = "C:/Users/pc/Downloads/chromedriver_win32 (1)/chromedriver.exe"
    # selenium의 webdriver로 크롬 브라우저를 실행한다
    driver = webdriver.Chrome(path)

    # 달빛학사에 접속 - gmail로 접속할지, id로 접속할지 입력받고 그에맞게 설정하지만, 우선 id-password 방법으로 로그인 하는 코드에요
    driver.get('https://go.sasa.hs.kr')
    time.sleep(1)
    driver.find_element_by_name('id').send_keys(user_id)
    time.sleep(1)
    driver.find_element_by_name('passwd').send_keys(user_password)
    driver.find_element_by_class_name('btn-info').click()
    time.sleep(2)

def is_free(target_name, time):
    # 해당 시간에 타겟이 공강인지 판별하여 공강이면 'True'를 아니면 'False'를 return 한다
    # 공강시간검색 창으로 이동
    time.sleep(2)
    driver.get('https://go.sasa.hs.kr/timetable/dup')
    # 타겟의 이름을 입력한다
    write_name = driver.find_element_by_class_name('form-control')
    write_name.send_keys(target_name)
    time.sleep(2)
    write_name.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    write_name.send_keys(Keys.ENTER)
    write_name.send_keys(Keys.ENTER)
    # 해당 시간에 공강인지 확인해준다
    titles = [
        element.text.strip()
        for element in driver.find_elements_by_id(time)
    ]
    if not titles:
        return False
    else:
        # 공강이므로 True 를 return 한다
        return True


