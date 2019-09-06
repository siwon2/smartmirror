def News(self,MainWindow) :
    d = feedparser.parse(self.News_url)
    while True :
        num = 1
        for e in d.entries :
            if num%10==1:
                self.news1.setText("[%d] %s"%(num,e.title))
            elif num%10==2:
                self.news2.setText("[%d] %s"%(num,e.title))
            elif num%10==3:
                self.news3.setText("[%d] %s"%(num,e.title))
            elif num%10==4:
                self.news4.setText("[%d] %s"%(num,e.title))
            elif num%10==5:
                self.news5.setText("[%d] %s"%(num,e.title))
            elif num%10==6:
                self.news6.setText("[%d] %s"%(num,e.title))
            elif num%10==7:
                self.news7.setText("[%d] %s"%(num,e.title))
            elif num%10==8:
                self.news8.setText("[%d] %s"%(num,e.title))
            elif num%10==9:
                self.news9.setText("[%d] %s"%(num,e.title))
            elif num%10==0:
                self.news10.setText("[%d] %s"%(num,e.title))
            num=num+1
            sleep(1)