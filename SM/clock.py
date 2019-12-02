def set_time(self,MainWindow):
    EvenOrAfter = "오전"
    while True:
        now=datetime.datetime.now() #현재 시각을 시스템에서 가져옴
        hour=now.hour

        if(now.hour>=12):
            EvenOrAfter="오후"
            hour=now.hour%12

            if(now.hour==12):
                hour=12

        else:
            EvenOrAfter="오전"

        self.date.setText("%s년 %s월 %s일"%(now.year,now.month,now.day))
        self.time.setText(EvenOrAfter+" %s시 %s분" %(hour,now.minute))
        sleep(1)