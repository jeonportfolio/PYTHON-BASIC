inFp = None 
fName, inList, inStr = "", [ ], ""   

fName = input("파일경로를  입력하세요 : ")
inFp = open(fName, "r", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end = "")

inFp.close()

