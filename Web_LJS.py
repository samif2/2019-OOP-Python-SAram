import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# chromedriver의 위치를 path에 저장한다
path = "C:/Users/pc/Downloads/chromedriver_win32 (1)/chromedriver.exe"
# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome(path)

# 달빛학사에 접속
driver.get('https://go.sasa.hs.kr')
time.sleep(1)
driver.find_element_by_name('id').send_keys('1862')
time.sleep(1)
driver.find_element_by_name('passwd').send_keys('samiff0926*')


driver.find_element_by_class_name('btn-flat').click()

time.sleep(2)
driver.find_element_by_name('identifier').send_keys('samif220020926@sasa.hs.kr')
time.sleep(2)
driver.find_element_by_id('identifierNext').click()
time.sleep(3)
driver.find_element_by_name('password').send_keys('samiff0926')
driver.find_element_by_id('passwordNext').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/ul/li[2]/a/span').click()
time.sleep(2)
write_name = driver.find_element_by_class_name('form-control')
write_name.send_keys("권정준")
time.sleep(2)
write_name.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
write_name.send_keys(Keys.ENTER)
write_name.send_keys(Keys.ENTER)