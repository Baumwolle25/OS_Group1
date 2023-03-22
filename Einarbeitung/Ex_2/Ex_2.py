from datetime import datetime
import time

class HelloWorld():

    def printHello(self):
        print("Hello")
    def printALot(self):
        for i in set("Welcome to my TED talk!"):
            print(i)
            time.sleep(0.5)
    def waitATon(self, timer):
        t1 = 0
        # src: https://stackoverflow.com/questions/28154066/how-to-convert-datetime-to-integer-in-python
        t2 = int(datetime.now().strftime('%Y%m%d%H%M%S')) + timer
        while t1 < t2:
            t1 = int(datetime.now().strftime('%Y%m%d%H%M%S'))
        print("loop finished")

    

a = HelloWorld()
a.printHello()
a.printALot()
a.waitATon(25)