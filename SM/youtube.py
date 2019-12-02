def Video_to_frame(self, MainWindow):
    url = "https://youtu.be/"

    api = yapi.YoutubeAPI('AIzaSyCzthYfSnRAsubOsPKyhDzYeEmn2iKjK5w')
    video_name="뉴스룸 모아보기"
    results = api.general_search(video_name, max_results=2)
    
    str_results=str(results)

    i=0
    TrueOrFalse=False
    video_id=""

    #print(str_results)
    
    while True:
        try :

            if "'" in str_results[i]:
                if "=" in str_results[i-1]:
                    if "d" in str_results[i-2]:
                        if "I" in str_results[i-3]:
                            if "o" in str_results[i-4]:
                                i=i+1
                                TrueOrFalse=True
                                break
            i=i+1

        except IndexError as e:
            print("error")
            break

    while TrueOrFalse:
        if "'" in str_results[i]:
            break
        else :
            video_id=video_id+str_results[i]

        i=i+1

    url = url+video_id

    try :
        vPafy = pafy.new(url)
        self.video_name_label.setText(vPafy.title)
        video_length=vPafy.length/60

    except Exception as e :
        self.video_viewer_label.setText("Error")
        self.start=False
    print(video_length/60)

    play = vPafy.getbest(preftype="mp4")
        
    cap = cv2.VideoCapture(play.url)

    while self.start:
        self.ret, self.frame = cap.read()
        if self.ret:
            self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
               
            self.pixmap = QPixmap(self.convertToQtFormat)
            self.p = self.pixmap.scaled(400, 225, QtCore.Qt.IgnoreAspectRatio)

            self.video_viewer_label.setPixmap(self.p)
            self.video_viewer_label.update()

            sleep(0.02) #Youtube 영상 1프레임당 0.02초

        else :
            break
            
        if self.start_or_stop:
            break

    cap.release()
    cv2.destroyAllWindows()