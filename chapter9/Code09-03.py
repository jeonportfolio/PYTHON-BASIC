coffee = 0

def coffee_machine(button) :
     print()
     print("#1. (자동) 뜨거운 물을 준비한다.");
     print("#2. (자동) 종이컵을 준비한다.");

     if button == 1 :
          print("#3. (자동) 보통커피를 탄다.")
     elif button == 2 :
          print("#3. (자동) 설탕커피를 탄다.")
     elif button == 3 :
          print("#3. (자동) 블랙커피를 탄다.")
     else :
          print("#3. (자동) 아무거나 탄다.\n")

     print("#4. (자동) 물을 붓는다.");
     print("#5. (자동) 스푼으로 젓는다.");
     print()

coffee = int(input("A손님 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("A손님  커피 여기 있습니다.")

coffee = int(input("B손님 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("B손님 커피 여기 있습니다.")

coffee = int(input("C손님 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("C손님 커피 여기 있습니다.")
