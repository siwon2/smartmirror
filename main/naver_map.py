from selenium import webdriver

from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

def Naver_map_way(start_point,end_point):
    opt =Options()
    opt.add_argument("--headless") 
    
    opt.add_experimental_option("prefs",
        {    
            "profile.default_content_setting_values.notifications": 1 
        }
    )
    driver = webdriver.Chrome('C:/Users/0308e/OneDrive/바탕 화면/chromedriver',chrome_options=opt)

    # driver.implicitly_wait(3)

    driver.get('https://map.naver.com/')

    a = driver.find_elements_by_class_name("nav_lst")[0]
    a.find_elements_by_xpath(".//*")[3].click()

    #pf_act 클래스가 생성되기전까지 기다림
    a_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pf_act")))

    b=driver.find_elements_by_class_name("pf_tab_public")[0]
    b.find_elements_by_xpath(".//*")[0].click()

    driver.find_elements_by_class_name('input_act')[1].send_keys(start_point)
    driver.find_elements_by_class_name('input_act')[1].send_keys(Keys.ENTER)

    sleep(0.2)
    driver.find_elements_by_class_name('input_act')[2].send_keys(end_point)
    driver.find_elements_by_class_name('input_act')[2].send_keys(Keys.ENTER)
    sleep(0.2)

    b=driver.find_elements_by_class_name("pf_act")[0]
    b.find_elements_by_xpath(".//*")[3].click()

    sleep(3)


    b = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fw_path_info2")))
    b.find_elements_by_xpath(".//*")[3].click()

    #fwp_path 클래스가 생성되기전까지 기다림
    way_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fwp_path")))
    time_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fwpout_r")))
    #경로 1의 경로
    way = driver.execute_script("return arguments[0].textContent", way_element)
    time = driver.execute_script("return arguments[0].textContent", time_element)

    way=way.replace("  ","")
    return time,way


way_map=Naver_map_way("대구소프트웨어고등학교","서울시청")
print("시간 + 요금 : "+way_map[0])
print("경로 : "+way_map[1])