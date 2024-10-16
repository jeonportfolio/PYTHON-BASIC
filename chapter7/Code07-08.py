# del ,len,sorted는 내장 함수이고 나머지는 메소드이다 (표7-1)
#튜플은 한번 저장하면 수정할수가 없는 것이다
#리스트로 변환하고 다시 튜플로 만들면 변환은 가능하다 다만 다른 튜플이 되는것
#딕셔너리에는 순서가 없다 

singer = {}

singer['이름'] = '트와이스'
singer['구성원수'] = 9
singer['데뷰'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for k in singer.keys() :
    print("%s --> %s" % (k, singer[k]))
