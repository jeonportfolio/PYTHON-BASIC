inFp = None    
inStr = ""        

inFp = open("chapter11/data1.txt", "r", encoding="UTF8")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
