outFp = None 
outStr = ""

outFp = open("chapter11/data1.txt", "w", encoding="UTF8")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break
outFp.close()
print("--- 파일에 정상적으로 써졌음 ---")
