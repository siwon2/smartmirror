
###
# the output layout is as follows:
# parsed --> [[surface, feature] for word in text]
# surface = 'surface'
# feature = ('품사, sub-class 1, sub-class 2, sub-class 3, (단어·언어의) 굴절[어미·어형 변화], conjugation, root-form, reading, pronunciation')
###
            
class MorphologyAnalyst():

    def __init__(self):
        import MeCab
        import re
        self.analyzed = []
        
        self.mecab_tagger  = MeCab.Tagger()
        self.expr_pattern = re.compile(r'(\w+)/(\w+)/.*?(?:\+|$)')
        self.space_pattern = re.compile(r'\s')
        self.word_class_dict = { #한글의 5언 dict
            'N' : '체언', 
            'V' : '용언',
            'M' : '수식언',
            'I' : '독립언',
            'J' : '관계언',
            'E' : '어미',   
            'X' : '접사',
            'S' : '부호'
        }
        self.exceptional_word_class_dict = { #예외적인 5언
            'XR' : '어근', 
            'SL' : '한글 이외',
            'SH' : '한글 이외',
            'SN' : '한글 이외'
        }
        self.part_of_speech_dict = {
            'NNG' : '일반 명사',
            'NNP' : '고유 명사',
            'NNB' : '의존 명사',
            'NNBC' : '단위를 나타내는 명사',
            'NR' : '수사',
            'NP' : '대명사',
            'VV' : '동사',
            'VA' : '형용사',
            'VX' : '보조 용언',
            'VCP' : '긍정 지정사',
            'VCN' : '부정 지정사',
            'MM' : '관형사',
            'MAG' : '일반 부사',
            'MAJ' : '접속 부사',
            'IC' : '감탄사',
            'JKS' : '주격 조사',
            'JKC' : '보격 조사',
            'JKG' : '관형격 조사',
            'JKO' : '목적격 조사',
            'JKB' : '부사격 조사',
            'JKV' : '호격 조사',
            'JKQ' : '인용격 조사',
            'JX' : '보조사',
            'JC' : '접속 조사',
            'EP' : '선어말 어미',
            'EF' : '종결 어미',
            'EC' : '연결 어미',
            'ETN' : '명사형 전성 어미',
            'ETM' : '관형형 전성 어미',
            'XPN' : '체언 접두사',
            'XSN' : '명사 파생 접미사',
            'XSV' : '동사 파생 접미사',
            'XSA' : '형용사 파생 접미사',
            'XR' : '어근',
            'SF' : '마침표', # .(온점) ?(물음표) !(느낌표)
            'SE' : '줄임표',  # ...
            'SSO' : '여는 괄호', 
            'SSC' : '닫는 괄호',
            'SC' : '구분자', # ,(쉼표) ·(가운뎃 점) /(빗금) :(쌍점)
            'SY' : '기타기호', 
            'SL' : '외국어',
            'SH' : '한자',
            'SN' : '숫자'}

    def remove_space(self, string):
        if isinstance(string, list):
            return list(map(self.remove_space, string))
        return self.space_pattern.sub('', string)
    def set_filter(self, features):
        if type(features).__name__ == 'SRE_Pattern':
            features = [features]
        if isinstance(features, str):
            features = [features]

        if isinstance(features[0], str): #string의 list인경우
            features = self.remove_space(features)
            filtered = {}
            for feat in features: #명사로 필터링할 경우 일반 명사와 대명사를 포함하게 됨.
                feat_filter = lambda x : self.remove_space(feat) in self.remove_space(x[1]) or self.remove_space(feat) in self.remove_space(x[2])
                filtered[feat]  = list(filter(feat_filter, self.analyzed))
            return filtered
        elif type(features[0]).__name__ == 'SRE_Pattern': #compile된 정규식 pattern의 리스트인 경우
            filtered = []
            for feat in features:
                filtered.append(feat.findall(self.joined))
            return filtered

    def analyze(self,text):
        self.analyzed = []
        parsed= self.parse(text)
        for i in parsed: 
            surface = i[0]
            feature = i[1]
            part_of_speech = self.part_of_speech_dict.get(feature[0])
            if part_of_speech is None:
                for i in self.expr_pattern.findall(feature[-1]):
                    surface =   i[0]
                    part_of_speech = self.part_of_speech_dict.get(i[1])
                    word_class = self.exceptional_word_class_dict.get(i[1]) #예외적인 word_class부터 확인
                    if word_class is None: 
                        word_class = self.word_class_dict.get(i[1][0]) 
                    self.analyzed.append([surface, word_class, part_of_speech])
            else:
                word_class = self.exceptional_word_class_dict.get(feature[0]) #예외적인 word_class부터 확인
                if word_class is None: 
                    word_class = self.word_class_dict.get(feature[0][0]) 
                      
                self.analyzed.append([surface,word_class, part_of_speech])
        self.joined = self.remove_space('+'.join(list(map(lambda x : '/'.join(x),self.analyzed))))
        print("joined:",self.joined)
        return self.analyzed
    

    def parse(self,text):
        parsed = [[chunk.split('\t')[0], chunk.split('\t')[1].split(',')] for chunk in self.mecab_tagger.parse(text).splitlines()[:-1]]
        print('parsed:', parsed)
        return parsed

if __name__ =='__main__':

    ma = MorphologyAnalyst()

    import re
    # import pyperclip    
    # text =  pyperclip.paste()
    text = "열 번의 만남보다 한 번의 이별이 더 값지다."
    write=False
    analyzed = ma.analyze(text)
    print('입력 문자열 :',text)
    print('형태소 분석 :',analyzed)
    if write:
        with open("test.txt", "a",encoding='utf-8') as myfile:
            myfile.write('입력 문자열 :'+text+'\n')
            myfile.write('형태소 분석 :'+str(analyzed)+'\n')
    features = ['체언','용언']

    print(str(features), ':',ma.set_filter(features))
