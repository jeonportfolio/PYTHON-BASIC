inFp = None	
inStr = ""		
lineNum = 1

inFp = open("chapter11/data1.txt", "r", encoding="UTF8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print("%d : %s" %(lineNum, inStr), end="")
    lineNum += 1

inFp.close()
