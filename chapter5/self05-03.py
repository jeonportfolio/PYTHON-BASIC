
num = 0
sosu = True

num = int(input(" 숫자를 입력하세요 : "))

for i in range(2, num) :
        if  num % i == 0 :
                sosu = False

if sosu == True :
        print(" %d는 소수입니다. " % (num))
else :
        print(" %d는 소수가 아닙니다. " % (num))