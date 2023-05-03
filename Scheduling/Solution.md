# Gruppe 1 Lösungen Signale, Interrupts, Scheduling

## Aufgabe 1

```

import signal
import datetime
import time
import random



def signal_handler1(signum, frame):  #erst Signal-Handler, der rechnet
    signal_name=signal.Signals(signum).name
    timestamp=datetime.datetime.now().strftime("%J-%m-%t %H-%M-%S")
    result = random.randint(1, 10)
    print(f"[{timestamp}] Signal {signal_name} erhalten.  Berechnungsergibniss : {result}")


def signal_handler2(signum, frame): # Signal-Handler, der blokiert
    # Signalblockierung
    blocked_signals = {signal.SIGTERM}
    
    signal_name=signal.Signals(signum).name
    timestamp=datetime.datetime.now().strftime("%J-%m-%t %H-%M-%S")
    signal.SIG_BLOCK
    # Eine Aufgabe erledigen
    input("Drücken Sie die Eingabetaste, um fortzufahren...")
    print(f"[{timestamp}] Signal {signal_name} erhalten. Ende der blockierender System-Call")


    # Signale entsperren
    signal.SIG_UNBLOCK

def signal_handler3(signum, frame):    ##erst Signal-Handler, der schläft
    signal_name=signal.Signals(signum).name
    timestamp=datetime.datetime.now().strftime("%J-%m-%t %H-%M-%S")
    print(f"[{timestamp}] Signal {signal_name} erhalten.  Beim Schlafen...")
    time.sleep(10)
    print(f"[{timestamp}] Signal {signal_name} erhalten.  Erwachen...")


signal.signal(signal.SIGUSR1, signal_handler1)
signal.signal(signal.SIGTERM, signal_handler2)
signal.signal(signal.SIGINT, signal_handler3)




while True:
    time.sleep(15)
    
    ```
    ```
    import signal
import os
import sys

class Terminate(BaseException):
    pass

def sigterm_exception(signalNumber, stackframe):
    raise Terminate()

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    raise SystemExit('Exiting')

    return


def run_main(main):
    import signal
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGINT, signal.SIG_IGN)  #Der Signal SIGINT wird ignoriert
    signal.signal(signal.SIGTERM, sigterm_exception)
    try:
        sys.exit(main(sys.argv[1:]) or 0)
    except Terminate:
        signal.signal(signal.SIGTERM, signal.SIG_DFL)  #Der Signal SIGTERM wird der Default-Verhalten
        os.kill(os.getpid(), signal.SIGTERM)


signal.pause() #Wart auf ein Signal
```

## Aufgabe 2

## Aufgabe 3

1. Schedule der Folie überprüfen

>nur-cpu.dat
```
0:1,-1
1:100,-1
2:1,-1
3:100,-1
```

>output
```
Laufzeiten:
PID Ankunft Rechenz Startze Endzeit TurnAro  Quotient
-----------------------------------------------------
  0       0       1       0       1       1    1.0000
  1       1     100       1     101     100    1.0000
  2       2       1     101     102     100  100.0000
  3       3     100     102     202     199    1.9900

```
2. Die Funktionen des Quellcodes
   
a. `create_process()`

Fügt der Prozessliste einen Prozess (Zeile in der *.dat file) hinzu.
Weist auserdem Startzeiten und pids zu.

b. `run_current()`

Läst den aktuellen Prozess eine Zeiteinheit "rechnen". 
Wenn die Zeit abgelaufen ist, wird er geblockt.

c. `update_blocked_processes()`

Reduziert den Timeout um eine Zeiteinheit.
Wenn der Timeout bei 0 ist, wird der Prozess wieder auf ready gesetzt oder beendet.

3. SJF-Scheduler

SJF_Scheduler.py
```

```


## Aufgabe 4

Abgaben von Anton Stimmer, Oscar Röth
