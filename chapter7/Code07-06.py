list1 = []
list2 = []
value=1
for i in range(0, 3) :
    for k in range(0, 4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    print("%s list1의 값 "%list1)
    print("%s list2의 값 " % list2)
    list1 = []

for i in range(0, 3) :
    for k in range(0, 4) :
        print("%3d" % list2[i][k], end = " ")
    print("")
