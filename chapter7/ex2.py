tt1 = (10,20,30) 
print(tt1)

tt2 = 10,20,30 
print(tt2)

tt3 = (10)
print(tt3)

tt1 = (10,20,30,40)
print(tt1[0])


#튜플을 변경하는 과정
myTuple = (10,20,30)
myList = list(myTuple)
myList.append(40)
myTuple= tuple(myList)
print(myTuple)