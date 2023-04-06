# Gruppe 1 Lösungen Prozesse & Threads

## Augabe 1

> fork

src: https://www.man7.org/linux/man-pages/man2/fork.2.html

Das Kommando `fork` erstellt einen `Child` Process, der zum Zeitpunkt des Erstellens mit seinem `Parrent` bis auf die `Process ID` und eine Reihe anderer Faktoren identisch ist.

>  execl

src: https://man7.org/linux/man-pages/man3/exec.3.html

Die `exec()` Funktions-Familie erstellt ein neues `Process Image` im laufenden Prozess, wobei `execl` von `execve` erbt und `const char *arg` als Argumente für die aufzurufende Funktion annimt, die `pointer` zu `null-terminated strings` sein müssen.

> waitpid

src: https://man7.org/linux/man-pages/man2/wait.2.html

Das `waitpid` Kommando pausiert die Ausführung des aktuellen Threads bis der/die durch die `pid` spezifizierte `child` Thread/s seinen Zustand ändern.

> clone 

src: https://man7.org/linux/man-pages/man2/clone.2.html

`clone` erstellt ähnlich zu `fork` einen `Child` Thread, hat dabei aber präzisere Kontrolle über den Vorgang, so dass zum Beispiel Threads erstellt werden können, die sich den `virtual adress` Raum teilen.

> system

src: https://man7.org/linux/man-pages/man3/system.3.html

`system` nutzt `fork` um einen `child` Prozess zu erstellen, der ein `shell` Kommando mithilfe von `execl` ausführt und dannach zum aktuellen Prozess zurückkehrt.

## Augabe 2

Ein Python Programm das seine Terminal-Argumente alle 10 Sekunden ausgiebt.

```
# https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments

import sys
import time

arguments = sys.argv
arguments.pop(0)

while True:
    time.sleep(10)
    print(arguments)
```

src: https://linuxg.net/how-to-kill-processes-in-linux-and-unix/

1) Dieses Programm wird zweimal aufgerufen mit `python3 Ex_2a.py Argument1 Argument2 &`.
2) Mit `jobs` kann man sich die Liste der laufenden Prozesse ausgeben lassen.
3) Mit `kill -STOP %x` den Prozess stopen, wobei `x` gleich der `jobID`.#
4) Mit `ps x` wobei `x` die `jobID` ist, lässt sich der Status abfagen, `S` für laufende Prozesse, `Ss` für gestoppte.
5) Mit `kill -CONT %x` den Prozess wieder starten, wobei `x` gleich der `jobID`.
6) Mit `kill -TERM %x` lässt sich ein Prozess beenden. Das kann mit `jobs` kontrolliert werden.

- Mit `ps` die `PID` der laufenden bash finden.
- Mit `kill -9 x` wobei x die `PID` der bash ist, die bash beenden.



## Aufgabe 3

> blocked -> running

Wenn ein Thread vom OS geblocked wird, wählt das OS einen anderen Thread, der ausgeführt wird. Das bedeutet, ein `blocked` Thread wird von Definiton aus nach Auflösung des `blocked` Grundes in den `ready` Zustand gesetzt um dem neuen laufenden Thread nicht zu schaden.

> ready -> blocked

Das OS blockiert einen Thread, wenn während der Laufzeit etwas passiert, auf das der Thread warten muss. Da ein Thread im `ready` Zustand auch inaktiv ist und blockert werden kann wenn das OS den Thread auswählt, braucht es eine Zustandsänderung `ready -> blocked` nicht, das ein System ordungsgemäß funktioniert.

## Aufgabe 4

## Aufgabe 5

Abgaben von Anton Stimmer, Oscar Röth