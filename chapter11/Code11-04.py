inFp = None 
inList, inStr = [], ""

inFp = open("chapter11/data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList :
    	print(inStr, end="") ## 기존에 저장된 리스트에 /n이포함 띄어쓰기 없애주기 위해서 end=""

inFp.close()

