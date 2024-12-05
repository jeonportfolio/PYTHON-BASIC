import threading

class Calc :
    number = ''
    def  __init__(self, number) :
        self.number = number

    def run(self) :
        hap = 0
        for i in range(0, self.number+1) :
            hap += i
        print("1+2+3+.....+", self.number, "=", hap)

calc1 = Calc(1000)
calc2 = Calc(100000)
calc3 = Calc(10000000)

th1 = threading.Thread(target = calc1.run)
th2 = threading.Thread(target = calc2.run)
th3 = threading.Thread(target = calc3.run)

th1.start()
th2.start()
th3.start()

