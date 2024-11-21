inFp = None
inStr = ""		

inFp = open("chapter11/data1.txt", "r", encoding="UTF8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end = "")

inFp.close()

