inFp = None 
inList, inStr = [ ], ""    
lineNum = 1

inFp = open("chapter11/data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList :
     print("%d : %s" %(lineNum, inStr), end = "")
     lineNum += 1

inFp.close()
