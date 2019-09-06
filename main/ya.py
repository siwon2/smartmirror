import analyze

a = analyze.Analyst()
aa =a.analyze("밀어야 서울에서 대구까지 가는 길 좀 알려 줘")
d = analyze.Driver(aa)
#print(aa)
e = d.find_element({'write':analyze.Regex('밀어야|미러야')})
if e is not None:

    print(e)
    d=e.after
    print(d)
    print('wa')
else:
    print('no?')