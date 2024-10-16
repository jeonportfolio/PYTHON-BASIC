

aa =[]
for i in range(0,100):
        aa.append(0)

print(len(aa))

aa = [10,20,30,40]
print("aa[-1]은 %d , aa[-2]는 %d" % (aa[-1],aa[-2]))

aa = [10,20,30,40]
print(aa[0:3],aa[2:4])

aa = [10,20,30,40]
print(aa[2:],aa[:2])

aa = [10,20,30]
aa[1] = 200
print(aa)

aa = [10,20,30]
aa[1:2] = [200,201]
print(aa)

aa = [10,20,30]
aa[1] = [200,201]
print(aa)

aa = [10,20,30]
del(aa[1])
print(aa)

aa =[10,20,30,40,50]
aa[1:4] = []
print(aa)


# del ,len,sorted는 내장 함수이고 나머지는 메소드이다 (표7-1)

