inFp = None 
inList = ""    

inFp = open("chapter11/data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
print(inList)

inFp.close()


 