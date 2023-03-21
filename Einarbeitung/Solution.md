# Gruppe 1 Lösungen Einarbeitung

## Augabe 1

## Aufgabe 2

```
import time

class HelloWorld():

    def printHello(self):
        print("Hello")
    def printALot(self):
        for i in set("Welcome to my TED talk!"):
            time.sleep(1)
            print(i)

a = HelloWorld()
a.printHello()
a.printALot()
```