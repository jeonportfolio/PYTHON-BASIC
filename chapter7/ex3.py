student1 = {'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
print(student1)

student1['연락처'] = '010-1111-2222'
print(student1)

print(student1.get('이름'))

print(student1.keys())

print(list(student1.keys()))

print(student1.values())

print(student1.items())