# Gruppe 1 Lösungen Einarbeitung

## Augabe 1

Um einen Befehl von Anfang an im Hintergrund auszuführen, ein & anfügen

`python3 /Ex_2/Ex_2.py &`

Um einen Befehl nach dem Ausführen in den Hintergrung zu bewegen:

`python3 /Ex_2/Ex_2.py`

Während der Ausführung: `control + Z` um den aktuell laufenden Befehl zu pausieren.

Mit `bg` den Befehl in den Hintergrund schieben und fortsetzen.

## Aufgabe 2

```
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
```