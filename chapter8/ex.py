ss="파이썬 최고"
print(ss[0])
print(ss[1:3])
print(ss[3:])

ss= '파이썬' + '최고' 
print(ss)
ss = '파이썬' * 3
print(ss)


dd = 'Python is Easy 그래서 programing이 재밌습니다'
print(dd.upper())
print(dd.lower())
print(dd.swapcase())#대문자는 소문자로 소문자는 대문자로
print(dd.title())


gg = '파이썬 공부는 재미 없습니다 모든 공부가 재미가 없죠^^'#rfind는 오른쪽부터 찾는것 인덱스의 숫자는 그대로 나온다 두번째 공부는 19번째에 위치
gg.count('공부')
print(gg.find('공부'),gg.rfind('공부'),gg.find('공부',5),gg.find('있다')) #문자가 없으면 -1이 반환 gg.find('공부',5)는 5부터이므로 두번째 공부가 해당
print(gg.index('공부'),gg.rindex('공부'),gg.index('공부',5))
print(gg.startswith('파이썬'), gg.startswith('파이썬',10),gg.endswith('^^'))


tt = ' 파  이  썬 '
tt.strip()
tt.rstrip()
tt.lstrip()

yy = '----파----이-----썬-----'
print(yy.strip('-'))
hh = '<<<파<<이<<<썬>>>>'
print(hh.strip('<>'))