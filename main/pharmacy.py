import json

class Pharmacy():
	def __init__(self):
		with open('pharmacy.json',encoding="utf8") as json_file:
			self.json_data = json.load(json_file)
	
	def prescribe(self, symptom):
		try:
			medicines = self.json_data[symptom]
			return medicines
		except KeyError:
			return None


# --------감지할수있는 증상----------
# 발열
# 두통
# 신경통
# 근육통
# 원결통
# 염좌통
# 코막힘
# 재채기
# 기침
# 인후통
# 가래
# 오한
# 관절통
# 목아픔
# 소화불량
# 식욕감퇴
# 과식
# 체함
# 소화촉진
# 어깨결림
# 요통
# 류마티스
# 타박상
# 삠
# 골절통