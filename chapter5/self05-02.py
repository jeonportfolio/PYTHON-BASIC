
answer, var1, var2, var3 = 0, 0, 0, 0


var1 = int(input(" 첫 번째 숫자를 입력하세요 : "))
var2 = int(input(" 두 번째 숫자를 입력하세요 : "))
var3 = int(input(" 더할 숫자를 입력하세요 : "))
for i in range(var1, var2+1, var3) :
        answer = answer + i
print(" %d+%d+...+%d는 %d입니다. " % (var1, var1+var3, var2, answer))
