number=0
count=0
result=0
i=0

number=int(input("시프트할 숫자는? "))
count=int(input("출력할 횟수는? "))

for i in range(1, count+1) :
    result = number << i
    print("%d << %d = %d" % (number, i , result))

for i in range(1, count + 1) :
    result = number >> i
    print("%d >> %d = %d" % (number, i , result))
