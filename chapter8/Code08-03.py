dd = input("입력 문자열 ==> ")
print("출력 문자열 ==> ", end = '')

if dd.startswith('(') == False :
     print("(", end = '')
print(dd, end ='')

if dd.endswith(')') == False :
     print(")", end = '')

