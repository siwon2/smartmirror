import os
from selenium import *
import selenium.webdriver as webdriver
from selenium.webdriver import *
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.options import *
from operator import methodcaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from PyQt5 import QtCore
# import time

class FaceBook(QtCore.QObject):
    isRunning = False
    def __init__(self,visible=False,email="facebook_id",password="facebook_password", signal=None):
        opt =Options()
        
        if not visible:
            opt.add_argument("--headless") 
        
        opt.add_experimental_option("prefs",
            {    
                "profile.default_content_setting_values.notifications": 1 
            }
        )
        self.email = email
        self.password =password
        self.signal = signal

        self.driver = webdriver.Chrome(chrome_options=opt)
    
    def register_handler(self,handler):
        self.isRunning = True
        self.handler =handler
        import threading
        t= threading.Thread(target=self.receive_new_msgs)
        t.daemon = True
        t.start()
        return t #쓰레드 반환함.

    def unregister_handler(self):
        self.isRunning = False
        self.handler = None
    
    

    def login(self):
        self.driver.get("https://www.facebook.com")

        self.driver.find_element_by_id("email").send_keys(self.email)
        self.driver.find_element_by_id("pass").send_keys(self.password)
        self.driver.find_element_by_id("loginbutton").click()
        self.msg_btn = self.driver.find_element_by_name("mercurymessages")

    def receive_new_msgs(self):
        while self.isRunning:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,\
                     "//*[@id='mercurymessagesCountValue'][not(contains(@class,'hidden_elem'))]"))
                )
            except:
                continue
            self.handler(self.read_msgs(), self.signal)

    def remove_new_msg_cnt(self, elem):
        self.msg_btn.click()
        elem.click()
    def read_msgs(self,only_new =True):
        contents = self.driver.find_elements_by_class_name("content")
        if contents == []:
            #contents읽어온게 없으면 메시지버튼을 눌러서 수동로드시켜야됨.

            #메시지창 열기
            self.msg_btn.click()

            #content로드 될때까지 기다리기
            # t= time.time()
        
            # print('wait....')
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "content"))
            )                                       
            # print("waited for %.1fs" % (time.time()-t))

            #메시지 창 닫기
            self.msg_btn.click()

            #콘텐츠들 일기
            contents = self.driver.find_elements_by_class_name("content")

        msgs=[]
        for content in contents:
            children = content.find_elements_by_xpath(".//text()/..") #text list는 에러나드라...
            inner_texts = list(map(methodcaller('get_attribute','innerText'),children))
                
            length = len(inner_texts)
            #상대방은 활성 text가 채팅방은 발신자 text가 포함될 수 있다.
            if length == 5:
                new_msg_cnt, author, sender, text, time =     inner_texts          
                sender = sender[:-len("님: "+text)]
                new_msg_cnt = int(new_msg_cnt[len(author+'('):-len(')')])
                
                self.remove_new_msg_cnt(content)
                msgs.append(               
                    {
                        'new_msg_cnt':new_msg_cnt, 
                        'author':author, 
                        'sender':sender, 
                        'text':text, 
                        'time':time
                    }
                )

            elif length == 4:
                if inner_texts[1] == '활성':
                    author, active, text, time = inner_texts
                    import re
                    match_object = re.match(r'(?P<author>.*)\((?P<new_msg_cnt>\d+)\)',author)
                    if match_object is None:  
                        if not only_new:      
                            msgs.append(               
                                {
                                    'author':author, 
                                    'active':active, 
                                    'text':text, 
                                    'time':time
                                }
                            )
                    else:
                        new_msg_cnt = match_object.groupdict()['new_msg_cnt']
                        author = match_object.groupdict()['author']
                        self.remove_new_msg_cnt(content)
                        msgs.append(               
                            {
                                'new_msg_cnt':new_msg_cnt, 
                                'author':author, 
                                'active':active, 
                                'text':text, 
                                'time':time
                            }
                        )
                else:
                    author, sender, text, time = inner_texts                
                    sender = sender[:-len("님: "+text)]
                    if not only_new:      
                        msgs.append(               
                            {
                                'author':author, 
                                'sender':sender, 
                                'text':text, 
                                'time':time
                            }
                        )
            
            elif length ==3:
                author, text, time = inner_texts
                if not only_new:      
                    msgs.append(               
                        {
                            'author':author, 
                            'text':text, 
                            'time':time
                        }
                    )
            else:
                assert 0

        self.remove_new_msg_cnt(self.msg_btn)
        return msgs

def handler(dicts, signal):
    for d in dicts:
        if 'sender' in d:
            #print('대화방 :',d['author'])
            #print('발신자 :',d['sender'])
            author = d['author']
            sender = d['sender']
            text = d['text']
            
            str_noti = author + " " + sender + " : " + text

            signal.emit("Facebook", str_noti)
        else:
            sender = d['author']
            text = d['text']

            str_noti = sender + " : " + text

            signal.emit("Facebook", str_noti)
        #print('내용 :',d['text'])
        #print('시간 :',d['time'])

if __name__ == '__main__':
    f=FaceBook()
    f.login()
    f.register_handler(handler)
    while True:
        pass
    # f.read_msgs()




