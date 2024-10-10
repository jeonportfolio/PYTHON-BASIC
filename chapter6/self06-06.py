hap = 0
a, b = 0, 0

while True:
    a = input("첫 번째 수를 입력하세요 : ")
    if a == "$":  
        break
    a = int(a)  

    b = int(input("두 번째 수를 입력하세요 : "))
    hap = a + b
    print("%d + %d = %d" % (a, b, hap))

print("프로그램 종료")