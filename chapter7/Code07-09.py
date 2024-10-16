import operator

trainDic, trainList = {}, []

trainDic = {'Thomas':'토마스', 'Edward':'에드워드', 'Henry':'헨리', 'Gothen':'고든', 'James':'제임스'} #키:값으로 정렬된 딕셔너리
trainList = sorted(trainDic.items(), key=operator.itemgetter(0))## 키값을 기준으로 오름차순 정렬이 됨 
print(trainList)
