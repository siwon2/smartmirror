import Map
import math
from selenium import webdriver

from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


def search(start, dest):
    opt = Options()
    opt.add_argument("--headless") 
    
    opt.add_experimental_option("prefs",
        {    
            "profile.default_content_setting_values.notifications": 1 
        }
    )
    driver = webdriver.Chrome('chromedriver',chrome_options=opt)

    # driver.implicitly_wait(3)

    driver.get('https://v4.map.naver.com/')
    driver.find_element_by_xpath("//button[@type='button' and @class='btn_close nclicks(popup.close)' and @onclick = 'window.closeDdayPopup()']").click()

    a = driver.find_elements_by_class_name("nav_lst")[0]
    a.find_elements_by_xpath(".//*")[3].click()

    #pf_act 클래스가 생성되기전까지 기다림
    a_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pf_act")))

    b=driver.find_elements_by_class_name("pf_tab_public")[0]
    b.find_elements_by_xpath(".//*")[0].click()

    driver.find_elements_by_class_name('input_act')[1].send_keys(start)
    driver.find_elements_by_class_name('input_act')[1].send_keys(Keys.ENTER)

    sleep(1)
    driver.find_elements_by_class_name('input_act')[2].send_keys(dest)
    driver.find_elements_by_class_name('input_act')[2].send_keys(Keys.ENTER)
    sleep(1)

    b=driver.find_elements_by_class_name("pf_act")[0]
    b.find_elements_by_xpath(".//*")[3].click()

    sleep(5)


    b = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fw_path_info2")))
    b.find_elements_by_xpath(".//*")[3].click()

    #fwp_path 클래스가 생성되기전까지 기다림
    way_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fwp_path")))
    time_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fpi_info")))
    #경로 1의 경로
    way = driver.execute_script("return arguments[0].textContent", way_element)
    time = driver.execute_script("return arguments[0].textContent", time_element)

    way=way.replace("  ","")
    way=way.replace("→","\n")
    time=time.replace("  ","")
    time=time.replace("|","\n")

    return time,way
