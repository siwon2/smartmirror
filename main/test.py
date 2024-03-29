from abc import *
import re
import json
from operator import methodcaller

from pprint import pprint as pp

import re
#보조용언이 아닌 용언을 찾는 패턴
predicate_pattern = re.compile(r'(?P<write>\w+)/용언/(?P<part_of_speech>((?!보조용언)\w)+)')
CV = ['되', '아니', '맞']
class SentenceStructure(metaclass=ABCMeta):

    @abstractmethod
    def as_dict(self):
        pass
    
    @abstractmethod
    def join(self):
        pass
        
    @abstractclassmethod
    def is_noun(self):
        pass

    def is_first(self, func):
        if func(self):
            self.first = self
            return True
        
        elif self.at(0) is not None and self.at(0).is_first(func):
            self.first = self.at(0).first
            return True

        return False
    
    @abstractmethod
    def append(self,cls):
        pass
    @abstractmethod
    def insert(self,index,cls):
        pass
    
    @abstractmethod
    def delete(self, index):
        pass

    @abstractmethod
    def at(self,index):
        pass

    def __getattribute__(self,name):
        try:
            return object.__getattribute__(self, name)
        except:
            if name == 'morphologys':
                return list(map(Morphology, self.join().split('+')))
            return None

    def __eq__(self,other):
        if isinstance(other,str):
            return other == self.class_name
        else:
            return object.__eq__(self, other)
    def __ne__(self,other):
        return not self.__eq__(other)

    def __str__(self):
        return json.dumps(self.as_dict(),ensure_ascii=False,indent=4)

class GrammaticalUnit(SentenceStructure):
            

    @staticmethod
    def construct(json_object):
        
        
        keys = list(json_object.keys())
        if keys == ['형태','문장']:
            return Clause(json_object)
        elif keys == ['형태', '문법단위들']:
            return Phrase(json_object)
        elif keys == ['형태소들']:
            return Word(json_object)
        elif keys == ['표기','언','품사']:
            return Morphology(json_object)
class SentenceComponent(SentenceStructure):
    class_name = '문장성분'
    def __init__(self, *args):
        if len(args)==3:
            self.role = args[0]
            self.grammatical_unit = args[1]
            self.postpositions = args[2]
            return 
        elif len(args)==2:
            self.role = args[0]
            self.grammatical_unit = args[1]
            self.postpositions = []
            return 
            
        elif isinstance(args[0],dict):
            json_object = args[0]
        elif isinstance(args[0], str):
            json_object = json.loads(args[0])
        self.role = json_object['역할'] 
        self.grammatical_unit = GrammaticalUnit.construct(json_object['문법단위'])
        self.postpositions = list(map(Word,json_object['조사들']))
    def is_adj(self):
        if self.role != '서술어':
            #서술어가 아닌데 호출하면 에러발생
            assert 0
        
        #보조용언이 아닌 용언들
        groupdicts = list(map(methodcaller('groupdict'),predicate_pattern.finditer(self.join())))
        
        if groupdicts == []:
            #보조용언으로만 이루어진거면 일단은 일반동사로 봄.
            #가지고 싶다가 보조용언 2개로 인식되더라.
            return False
        elif len(groupdicts) > 1:
            #흠.. 이건 에러아닌가?
            assert 0

        return groupdicts[0]['part_of_speech'] == '형용사'

    def is_cv(self):
        if self.role != '서술어':
            #서술어가 아닌데 호출하면 에러발생
            assert 0
        
        #보조용언이 아닌 용언들
        groupdicts = list(map(methodcaller('groupdict'),predicate_pattern.finditer(self.join())))
        
        if groupdicts == []:
            #보조용언으로만 이루어진거면 일단은 일반동사로 봄.
            #가지고 싶다가 보조용언 2개로 인식되더라.
            return False
        elif len(groupdicts) > 1:
            #흠.. 이건 에러아닌가?
            assert 0
            
        return groupdicts[0]['write'] == Regex('|'.join(CV))
     
    def is_noun(self):
        return self.grammatical_unit.is_noun()
    def at(self,index):
        return self.grammatical_unit.at(index)
    def insert(self, index, grammatical_unit):
        self.grammatical_unit.insert(index, grammatical_unit)
    def delete(self,index):
        self.grammatical_unit.delete(index)
    def append(self,grammactical_unit):
        self.grammatical_unit.append(grammactical_unit)
    def join(self):
        return '+'.join(list(map(methodcaller('join'),[self.grammatical_unit]+self.postpositions )))
    def as_dict(self):
        if self.postpositions == []:
            return {'역할':str(self.role),'문법단위': self.grammatical_unit.as_dict()}

        return {'역할':str(self.role),'문법단위': self.grammatical_unit.as_dict(), '조사들': list(map(methodcaller('as_dict'),self.postpositions))}



class Sentence(SentenceStructure):
    
    class_name ='문장'
    def __init__(self, *args):
        if isinstance(args[0],list):
            self.sentence_components = args[0]
            #한국어는 동사 V대신 서술어인 Predicate의 앞글자 P를 씀.
            return 
        elif isinstance(args[0],dict):
            json_object = args[0]
        elif isinstance(args[0], str):
            json_object = json.loads(args[0])
        self.sentence_components = list(map(SentenceComponent,json_object['문장성분들']))

    def assign_roles(self ):
        if self.cnt_dict['N'] ==0:
            return 
        
        roles = []
        
        if not self.p_is_adj:
            if self.p_is_cv:
                if self.cnt_dict['C'] ==0:
                    roles.append('보어')
            else:
                if self.cnt_dict['O'] ==0:
                    roles.append('목적어')

        if self.cnt_dict['S']==0:
            roles.append('주어')

        for i in list(self.N.keys()):
            
            self.sentence_components[i].role = roles.pop() if len(roles) > 0 else '부사어'

    def completion_test(self):
        self.S = {};self.O = {};self.C= {};self.P = {};self.N ={} 
        i=0
        for i in range(0, len(self.sentence_components)):
            sentence_component = self.sentence_components[i]
            if sentence_component.role is None:
                self.N[i] = sentence_component
            elif sentence_component.role == '주어':
                self.S[i] = sentence_component
            elif sentence_component.role == '목적어':
                self.O[i] = sentence_component
            elif sentence_component.role == '보어':
                self.C[i] = sentence_component
            elif sentence_component.role == '서술어':
                self.P[i] = sentence_component
                self.p_is_adj = sentence_component.is_adj() # 서술어가 형용사인지
                self.p_is_cv = sentence_component.is_cv() #서술어가 보어동사인지
        self.cnt_dict = {
            'S':len(self.S), 
            'O+C':len(self.O)+len(self.C), 
            'O':len(self.O),
            'C':len(self.C), 
            'P':len(self.P), 
            'N': len(self.N) #역할이 None인 것은 전부 Noun임.
        }
        if self.cnt_dict['N'] > 0:
            #역할이 정해지지않은 성분이 있으면 return False
            return False
        elif self.cnt_dict['P'] !=1 :
            #서술어는 한 개가 아니라면
            return False
        elif self.cnt_dict['S'] > 1 or self.cnt_dict['O+C'] > 1:
            #주어가 1개 초과 또는 목적어나 보어가 1개초과이면
            return False
        elif self.p_is_adj and self.cnt_dict['O+C'] > 0:
            #형용사인데 목적어나 보어를 가지면 
            return False
        
        elif self.p_is_cv and self.cnt_dict['O'] > 0 :
            #보어동사인데 목적어를 가지면 
            return False
        elif not self.p_is_cv and self.cnt_dict['C'] > 0:
            #보어동사가 아닌데 보어를 가지면
            return False
        elif self.cnt_dict['S'] ==1:
            #S의 인덱스
            index = list(self.S.keys())[0]
            #O+C의 인덱스들
            indexes = list(self.O.keys())+list(self.C.keys())
            return not any(index > i for i in indexes ) #목적어나 보어 중 하나라도 주어 앞에 있으면 False를 반환함.
        else:
            return True


    def at(self,index):
        return self.sentence_components[index]
    def insert(self, index, grammatical_unit):
        self.sentence_components.insert(index, grammatical_unit)
    def delete(self,index):
        del self.sentence_components[index]
    def append(self,grammatical_unit):
        self.sentence_components.append(grammatical_unit)
    
    #Sentence의 is_noun은 콜돼선 안됨.
    def is_noun():
        assert 0
    
    def join(self):
        return '+'.join(list(map(methodcaller('join'), self.sentence_components)))
    def as_dict(self):
        return {'문장성분들': list(map(methodcaller('as_dict'),self.sentence_components))}
    

class Clause(GrammaticalUnit):
    class_name = '절'
    def is_noun(self):
        return self.type =='명사절'
    def __init__(self, *args):
        if len(args)==2:
            self.type = args[0]
            self.sentence = args[1]
            return 
        elif isinstance(args[0],dict):
            json_object = args[0]
        elif isinstance(args[0], str):
            
            json_object = json.loads(args[0])
        self.type = json_object['형태']
        
        self.sentence = Sentence(json_object['문장'])
    
    def at(self,index):
        return self.sentence.at(index)
    def insert(self, index, sentence_component):
        self.sentence.insert(index, sentence_component)
    def delete(self,index):
        self.sentence.delete(index)
    def append(self,sentence_component):
        self.sentence.append(sentence_component)

    def join(self):
        return self.sentence.join()
    def as_dict(self):
        return {'형태':self.type,'문장': self.sentence.as_dict()}

class Phrase(GrammaticalUnit):
    class_name = '구'
    def is_noun(self):
        return self.type =='명사구'
    def __init__(self, *args):
        if len(args)==2:
            self.type = args[0]
            self.grammatical_units = args[1]
            return 
        elif isinstance(args[0],dict):
            json_object = args[0]
        elif isinstance(args[0], str):
            
            json_object = json.loads(args[0])

        self.type = json_object['형태']
        
        self.grammatical_units = list(map(GrammaticalUnit,json_object['문법단위들']))
    def at(self,index):
        return self.grammatical_units[index]
    def insert(self, index, grammatical_unit):
        self.grammatical_units.insert(index, grammatical_unit)
    def delete(self,index):
        del self.grammatical_units[index]
    def append(self,grammatical_unit):
        self.grammatical_units.append(grammatical_unit)

    def join(self):
        return '+'.join(list(map(methodcaller('join'), self.grammatical_units)))
    def as_dict(self):
        return {'형태':self.type,'문법단위들': list(map(methodcaller('as_dict'),self.grammatical_units))}


class Word(GrammaticalUnit):
    class_name = '단어'
    def is_noun(self):
        return self.at(-1) == Regex(r'\w+/체언/\w+|\w+/\w+/명사형전성어미|\w+/\w+/명사파생접미사')

    def __init__(self, *args):
        if isinstance(args[0],list):
            self.morphologys = args[0]
            return
        elif isinstance(args[0],dict):
            json_object = args[0]
        elif isinstance(args[0],str):
            json_object = json.loads(args[0])
        self.morphologys = list(map(Morphology,json_object['형태소들']))
    def at(self,index):
        return self.morphologys[index]
    def insert(self, index, morphology):
        self.morphologys.insert(index, morphology)
    def delete(self,index):
        del self.morphologys[index]
    def append(self,morphology):
        self.morphologys.append(morphology)

    def join(self):
        return '+'.join(list(map(methodcaller('join'), self.morphologys)))
    def as_dict(self):
        return {'형태소들': list(map(methodcaller('as_dict'),self.morphologys))}

class Regex():
    def __init__(self, pattern, groups=None):
        self.pattern = pattern
        self.groups = groups
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, str):
            if type(self.pattern).__name__ == "SRE_Pattern":
                match_object = self.pattern.match(other.replace(" ",""))

            else:
                import re
                match_object = re.match(self.pattern,other.replace(" ",""))
                
        elif isinstance(other, SentenceStructure):
            if type(self.pattern).__name__ == "SRE_Pattern":
                
                match_object = self.pattern.match(other.join())
            else:
                import re
                match_object = re.match(self.pattern,other.join())
                
        if self.groups is not None and match_object: 
            #groups와 match_object 둘다 None이 아니면
            #matches는 groups에 

            self.groups.extend(match_object.groups())
        # 반환은 True, False로만
        return match_object is not None


    def __ne__(self,other):
        return not self.__eq__(other)

class Morphology(GrammaticalUnit):
    
    class_name = '형태소'
    def is_noun(self):
        return self.word_class == '체언'
    def __init__(self, *args):
        if len(args)==3:
            self.write = args[0]
            self.word_class = args[1]
            self.part_of_speech = args[2]
            return
        elif isinstance(args[0],dict):
            json_object = args[0]
            self.write = json_object['표기']
            self.word_class = json_object['언']
            self.part_of_speech =json_object['품사']
        elif isinstance(args[0],str):
            self.write,self.word_class,self.part_of_speech = args[0].split('/')

    #Morphology의 insert와 delete,append는 호출해서는 안됨    
    def at(self, index):
        #얘는 is_first에서 써서 return None으로 바꿨음
        return None
    def insert(self, index, cls):
        assert 0
    
    def delete(self,index):
        assert 0
    def append(self,cls):
        assert 0
    
    def join(self):
        return '{}/{}/{}'.format(self.write, self.word_class, self.part_of_speech).replace(" ","")
        

    def as_dict(self):
        return '{}/{}/{}'.format(self.write, self.word_class, self.part_of_speech).replace(" ","")
        return {'표기':self.write, '언':self.word_class, '품사':self.part_of_speech}
    


###
# the output layout is as follows:
# parsed --> [[write, feature] for word in text]
# write = 'write'
# feature = ('품사, sub-class 1, sub-class 2, sub-class 3, (단어·언어의) 굴절[어미·어형 변화], conjugation, root-form, reading, pronunciation')
###
from re import split

class Analyst():

    def __init__(self):
        import MeCab
        import re
        analyzed = []
        self.string_set = []
        
        self.mecab_tagger  = MeCab.Tagger()
        self.expression_pattern = re.compile(r'(\w+)/(\w+)/.*?(?:\+|$)')
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
            'NN' : '명사',  
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


    def get_morphologys(self,text):
        self.morphologys = []
        parsed= self.parse(text)
        for i in parsed: 
            write = i[0]
            feature = i[1]
            part_of_speech = self.part_of_speech_dict.get(feature[0])
            if part_of_speech is None:
                for i in self.expression_pattern.findall(feature[-1]):
                    write =   i[0]
                    part_of_speech = self.part_of_speech_dict.get(i[1])
                    word_class = self.exceptional_word_class_dict.get(i[1]) #예외적인 word_class부터 확인
                    if word_class is None: 
                        word_class = self.word_class_dict.get(i[1][0]) 
                    self.morphologys.append(Morphology(write, word_class, part_of_speech))
            else:
                word_class = self.exceptional_word_class_dict.get(feature[0]) #예외적인 word_class부터 확인
                if word_class is None: 
                    word_class = self.word_class_dict.get(feature[0][0]) 
                      
                self.morphologys.append(Morphology(write,word_class, part_of_speech))
    
        return self.morphologys

    def parse(self,text):
        parsed = [[chunk.split('\t')[0], chunk.split('\t')[1].split(',')] for chunk in self.mecab_tagger.parse(text).splitlines()[:-1]]
        # print('parsed:', parsed)
        return parsed
    
    def remove_space(self, string):
        if isinstance(string, list):
            return list(map(self.remove_space, string))
        return self.space_pattern.sub('', string)
    def analyze(self,text):
        analyzed = self.get_morphologys(text)
        # print(Phrase(None,analyzed).join())
        i=0

        #어미와 접사를 합쳐서 단어 리스트로 변경
        while i < len(analyzed):
            groups=[]
            if i+1 == len(analyzed):
                pass
            

            elif analyzed[i+1].part_of_speech == Regex(r'\w+어미|(\w+)파생접미사',groups):
                if groups[0] is not None:
                    if groups[0] in ['동사','형용사']:
                        analyzed[i] = Morphology(analyzed[i].write+analyzed[i+1].write, '용언',groups[0])
                        del analyzed[i+1]
                    elif groups[0]  == ['명사']:
                        analyzed[i] = Morphology(analyzed[i].write+analyzed[i+1].write, '체언',groups[0])
                        del analyzed[i+1]
                    else: assert 0
                elif analyzed[i] == '단어':
                    analyzed[i].append(analyzed[i+1])
                    del analyzed[i+1]
                elif analyzed[i] == '형태소':
                    analyzed[i] = Word([analyzed[i],analyzed[i+1]])
                    del analyzed[i+1]
                else: assert 0
                continue

            elif analyzed[i].part_of_speech == Regex('체언접두사'):
                analyzed[i+1].write = analyzed[i].write + analyzed[i+1].write
                analyzed[i] = Word([analyzed[i+1]])
                del analyzed[i+1]
                continue
            
            if analyzed[i] == '형태소':
                if analyzed[i].word_class == '부호':
                    del analyzed[i]
                    continue
                else:
                    analyzed[i] =Word([analyzed[i]])

            i+=1

        #동사구를 만듦.
        i=0
        while i < len(analyzed):
            if i+1 == len(analyzed):
                pass
            elif analyzed[i].morphologys[0].word_class ==Regex('용언') and analyzed[i+1].morphologys[0].part_of_speech==Regex('보조용언'):
                if analyzed[i] == '구':
                    analyzed[i].append(analyzed[i+1])
                else:
                    analyzed[i] = Phrase('동사구', [analyzed[i],analyzed[i+1]])
                del analyzed[i+1]
                continue
            
            i+=1
        #절 만들기
        i=0
        while i < len(analyzed):
            if i+1 == len(analyzed):
                pass
        
            groups = []
            if analyzed[i].morphologys[-1] == Regex(r'\w+/\w+/(\w+)형전성어미',groups):
                sentence_component = SentenceComponent('서술어', analyzed[i])
                sentence = Sentence([sentence_component])
                clause = Clause(groups[0]+'절',sentence)
                if groups[0] == '명사':
                    analyzed[i] = SentenceComponent(None,clause)

                else:
                    analyzed[i] = SentenceComponent(groups[0]+'어', clause)
            
            i+=1
       
        #문장성분들을 만듦.
        i=0
        while i < len(analyzed):
            groups = []
            
            if i+1 == len(analyzed):
                pass
            elif analyzed[i+1].morphologys[0] == Regex(r'이/용언/긍정지정사'):
                #서술격조사 ~이다와 붙은 체언은 목적어로 둠.
                #또 서술격조사는 용언으로 보기도 해야하므로 체언에는 서술격조사로, 어미앞에서는 용언으로 붙게하였음
                analyzed[i] = SentenceComponent('목적어',analyzed[i],[Morphology('이','관계언','서술격조사')])
                i+=1
                continue
            elif analyzed[i+1].morphologys[0] == Regex(r'(\w+)/\w+/(\w+)격조사', groups):
                if groups[0] in ['이','가']: #이,가 주격조사는 pass
                    i+=1
                    continue
                analyzed[i] = SentenceComponent(groups[1]+'어',analyzed[i],[analyzed[i+1]])
                del analyzed[i+1]
                continue
                
           

            if analyzed[i] == Regex(r'\w+/독립언/\w+'):
                analyzed[i] = SentenceComponent('독립어',analyzed[i])
            elif analyzed[i] == Regex(r'\w+/\w+/\w+부사'):
                analyzed[i] = SentenceComponent('부사어',analyzed[i])
            elif analyzed[i] == Regex(r'\w+/\w+/관형사'): 
                analyzed[i] = SentenceComponent('관형어',analyzed[i])
            
            elif analyzed[i].morphologys[0].word_class == '용언': # elif analyzed[i] == Regex(r'\w+/용언/\w+\+(?:\w+/\w+/\w+\+)*\w+/\w+/(\w+)',groups) and groups[0] == '종결어미':
                
                if i+1 == len(analyzed):                          
                    # 가장 마지막에 위치하면 무조건 서술어로 봄 
                    analyzed[i] = SentenceComponent('서술어',analyzed[i])
                elif analyzed[i] == Regex(r'\w+/용언/\w+\+(?:\w+/\w+/\w+\+)*\w+/\w+/(\w+)',groups) \
                    and groups[0] != Regex('종결어미|\w+형전성어미'):  
                     #용언으로 시작하여 종결어미나 전성어미로 끝나지 않는 어미는 모두 부사절의 서술어로 봄.
                    sentence_component = SentenceComponent('서술어', analyzed[i])
                    sentence = Sentence([sentence_component])
                    clause = Clause('부사절',sentence)
                    analyzed[i] = SentenceComponent('부사어', clause,[])

            i+=1

        #문장성분 만들기 2
        i=0
        while i < len(analyzed):
            groups = []
            
            if i+1 == len(analyzed):
                pass
            elif analyzed[i+1].morphologys[0] == Regex(r'(이|가)/\w+/(\w+)격조사', groups):
                first_not_adv = next(i for i in analyzed[i+2:] if i.role != '부사어')
                if first_not_adv.morphologys[0] == Regex(r'{}/용언/\w+'.format('|'.join(CV))):
                    analyzed[i] = SentenceComponent('보어',analyzed[i],[Morphology(groups[0],'관계언','보격조사')])
                else:
                    analyzed[i] = SentenceComponent('주어',analyzed[i],[Morphology(groups[0],'관계언','주격조사')])
                del analyzed[i+1]
                continue
            elif analyzed[i] == '문장성분' and analyzed[i+1] == Regex(r'\w+/관계언/보조사'):
                #이시점에서 
                analyzed[i].postpositions.append(analyzed[i+1])
                del analyzed[i+1]
                    
                continue
                
            elif analyzed[i] == '단어' and analyzed[i+1] == Regex(r'\w+/관계언/보조사'):
                analyzed[i] = SentenceComponent(None, analyzed[i], [analyzed[i+1]])
                del analyzed[i+1]
                continue
            
            
            if analyzed[i] == '단어':
                analyzed[i] = SentenceComponent(None, analyzed[i])
               
            i+=1

        i=0
        
        # 구 만들기
        for j in range(0,2):
            i=0
            while i < len(analyzed):
                if i+1 == len(analyzed):
                    break
                if analyzed[i].role != '독립어' and analyzed[i] == Regex('\w+/체언/\w+') and analyzed[i].postpositions == [] and\
                    analyzed[i+1].role != '독립어' and analyzed[i+1].is_noun() and analyzed[i+1].postpositions != []:
                    if analyzed[i+1].grammatical_unit == '구':
                        analyzed[i+1].grammatical_unit.insert(0,analyzed[i])
                    else:
                        phrase =Phrase('명사구',[analyzed[i],analyzed[i+1].grammatical_unit])
                        analyzed[i+1].grammatical_unit = phrase
                        
                    del analyzed[i]
                    i=0
                    continue
               
                elif analyzed[i].role =='관형어' and analyzed[i+1].grammatical_unit == Regex(r'\w+/체언/\w+'):
                    phrase = Phrase('명사구',[analyzed[i],analyzed[i+1].grammatical_unit])
                    analyzed[i+1].grammatical_unit = phrase
                    del analyzed[i]

                    i=0
                    
                    # print('290:',Phrase(None,analyzed))
                    continue
            
                elif analyzed[i].role == analyzed[i+1].role =='관형어':
                    phrase = Phrase('관형구',[analyzed[i], analyzed[i+1]])
                    
                    sentence_component = SentenceComponent("관형어", phrase)
                    analyzed[i] =sentence_component
                    del analyzed[i+1]
                    
                    i=0
                    continue
                elif analyzed[i].role == analyzed[i+1].role =='부사어' and analyzed[i+1].grammatical_unit != '절':
                    phrase = Phrase('부사구',[analyzed[i], analyzed[i+1]])
                    
                    sentence_component = SentenceComponent("부사어", phrase)
                    analyzed[i] =sentence_component
                    del analyzed[i+1]
                    
                    i=0
                    continue
                elif analyzed[i].role != '독립어' and analyzed[i+1].is_first(lambda cls: cls.grammatical_unit == '절'):
                    if analyzed[i].grammatical_unit.is_noun():
                        sentence = analyzed[i+1].first.grammatical_unit.sentence 
                        sentence.completion_test()
                        if sentence.p_is_adj:
                            #형용사가 서술어인 경우  
                            pass
                        else:
                            tmp = analyzed[i].role
                            if analyzed[i].role is None:
                                #역할이 None인 경우
                                #목적어나 보어로 봄.
                                analyzed[i].role = '보어' if sentence.p_is_cv else '목적어'
                            
                            # analyzed[i+1].insert(0,analyzed[i])
                            analyzed[i+1].first.insert(0,analyzed[i])
                            if sentence.completion_test():
                                del analyzed[i] 
                                i=0
                                continue
                            else:
                                analyzed[i].role = tmp
                                # analyzed[i+1].delete(0)
                                analyzed[i+1].first.delete(0)
                    else:
                        # analyzed[i+1].insert(0,analyzed[i])
                        analyzed[i+1].first.insert(0,analyzed[i])
                        del analyzed[i]
                        
                        i=0
                        continue
                i+=1

            #none 없애기
            whole_sentence =Sentence(analyzed)
            whole_sentence.completion_test()
            whole_sentence.assign_roles()



        print(whole_sentence)
        return whole_sentence
        

            
    




if __name__ =='__main__': 
    ma = Analyst()
    
    ma.analyze('두통에 좋은 약 추천해줘')
    

  
