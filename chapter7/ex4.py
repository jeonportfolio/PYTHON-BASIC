aa = [10,20,30,40,50]
print(aa[0])
print(aa[1:3])
print(aa[3:])

numList = []
for num in range(1,6):
    numList .append(num)
print(numList) 

numList = [num for num in range(1,6)]
print(numList)

numList = [num for num in range(1,21) if num % 3 == 0]
print(numList)

foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨' , '삼겹살']
sides = ['오뎅', '단무지', '김치']
tupList = list(zip(foods, sides))
dic = dict(zip(foods, sides))
print(tupList)
print(dic)

oldList = ['짜장면', '탕수육', '군만두']
foodList = oldList
print(foodList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(foodList)


#깊은복사 [:]의 의미는 처음부터 끝이라는 뜻 스택은 그냥 자세히 알필요는 없음 
oldList = ['짜장면', '탕수육', '군만두']
food1List = oldList[:]
print(food1List)
oldList[0]= '짬뽕'
oldList.append('깐풍기')
print(food1List)

