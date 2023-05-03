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
Die Signal, die man skicken können sind:
kill -s SIGUSR1 <pid>  
Um die Rechnung zu machen
 
kill -s SIGTERM <pid>
Um ein blockierender System-Call zu haben
    
kill -s SIGINT <pid>
Um 10 Sekunden zu schlafen 

Man muss <pid> durch das Nummer der Prozess erzetzen
    
 1.a) Wenn man einmalig ein Signal senden möchte, während er schläft / arbeitet / blockiert ist, wird dieses Signal ausgeführt und nach Beendigung des Programms geht es weiter, wo es aufgehört hat.

1.b) Es ist das gleiche System wie zuvor: Das letzte gesendete Signal wird ausgeführt, dann das vorletzte und so weiter, bis das erste gesendete Signal beendet ist und das Hauptprogramm weiter ausgeführt werden kann.

1.c)
```    
import os
import signal

pid = 1234  # Ersetzen 1234 durch die PID des Zielprozesses.
sig = signal.SIGUSR2

os.kill(pid, sig)
```
Wenn der Zielprozess keinen Signalhandler für das SIGUSR2-Signal registriert hat, wird das Signal vom Prozess ignoriert und es werden keine Aktionen ausgeführt.
   
2) Man kann wählen, welches Signal man senden will und an welchen Prozess (pid)
    
3) Normalerweise nicht, weil das Programm auf meinem Computer läuft, aber wenn die beiden Computer verbunden sind (der Ping funktioniert), dann kann es in diesem Fall funktionieren oder wenn das Programm auf einem Server läuft, wo andere Benutzer sich einloggen und auf die Pid zugreifen können und genügend Rechte haben, um auf das Programm zuzugreifen (ihm ein Signal zu senden).

4)Der folgende Code ist ein Beispiel dafür, wie Sie ein Signal ignorieren und ein Standardsignal implementieren können.
    
    
```
import signal
import os
    
orig_handler = signal.signal(signal.SIGTERM, my_handler)

def my_handler(signum, frame):
  prnit("OK")

  # Jetzt tut man alles, was wir getan hätten, wenn my_handler nicht installiert worden wäre:

  if callable(orig_handler):              # Vorherigen Handler aufrufen
    orig_handler(signum, frame)
  elif orig_handler == signal.SIG_DFL:    # Standard-Disposition
    signal.signal(signum, signal.SIG_DFL)
    os.kill(os.getpid(), signum)
  else:
    signal.signal(signum, signal.SIG_IGN)  # letzlich SIG_IGN - nichts tun
                                          
signal.pause() #Wart auf ein Signal
```

## Aufgabe 2

1) Es gibt drei Hauptarten von Interruption:
    Externe (unabhängig vom Prozess) Eingriffe des Bedieners, Pannen, etc.
    Interne Fehler des Prozessors, Überlauf, Division durch Null, Seitenfehler usw. (Ursachen, die dazu führen, dass ein Backup des "core dumped"  Speicherabbilds auf Festplatte erstellt wird).
    Systemaufrufe, die eine Eingabe/Ausgabe anfordern, zum Beispiel.
   
     Aber alle folgen einer der beiden Arten von Interrupt-Anforderungen, entweder NMI: (No masquable interrupt) oder MI (masquable interrupt).
    
    Ablauf eines NMI:
    1- Alle Flags werden gespeichert, um ihren Wert zu sichern.
    2-Der IF-Index (Interrupt Flag) wird auf 0 gesetzt. 
    3- Der TF-Index (Trap Flag) wird auf 0 gesetzt. 
    4- Der Mikroprozessor stapelt die Register CS und IP auf dem Stack.
        5- Der Mikroprozessor lädt das Register IP mit dem 16-Bit-Wert, der sich an der Speicheradresse 00008H im Interrupt-Vektor befindet, und das Register CS (code segment) wird anschließend mit dem 16-Bit-Wert geladen, der sich an der Adresse 0000AH befindet.
     6- der Mikroprozessor zeigt nun auf das Interruptprogramm, das er ausführen wird, und kehrt dann zu seinem Hauptprogramm zurück.
    
    Ablauf einer maskierbaren Unterbrechung :

    1- Ein INT-Signal wird von einem Gerät (oder von der Schnittstelle, die das Gerät verwaltet) gesendet.
    2- Der Interrupt-Controller empfängt dieses Signal an einem seiner IRQi-Klemmen (interrupt request). Sobald es möglich ist (abhängig von anderen Interrupts, die auf ihre Verarbeitung warten), sendet der Controller ein Signal an seinen INT-Anschluss.
    3- Der Mikroprozessor berücksichtigt das Signal an seiner INTR-Klemme, nachdem er die Ausführung des aktuellen Befehls abgeschlossen hat (was einige Taktzyklen dauern kann). Wenn der Indikator IF=0 ist, wird das Signal ignoriert, andernfalls wird die Interrupt-Anforderung akzeptiert.
    4- Wenn die Anfrage angenommen wird, setzt der Mikroprozessor seinen INTA-Ausgang für 2 Taktzyklen auf 0, um dem Controller zu signalisieren, dass er seine Anfrage berücksichtigt.
    5- Als Antwort legt der Interrupt-Controller die mit dem IRQi-Anschluss verbundene Interrupt-Nummer auf den Datenbus.
    6- Der Prozessor liest die Interruptnummer auf dem Datenbus und verwendet sie, um den Interruptvektor zu finden.
    7- Der Prozessor speichert die Indikatoren des Statusregisters auf dem Stack
    8- der Prozessor setzt den IF-Indikator auf 0 (verbirgt die folgenden Interrupts)
    9- Der Prozessor speichert CS und IP auf dem Stack
    10- Der Prozessor sucht in der Interruptvektortabelle nach der Adresse des Interruptbearbeiters und lädt sie in CS:IP.
    11. Die Prozedur, die den Interrupt verarbeitet, läuft ab. Währenddessen werden die Interrupts ausgeblendet (IF=0). Wenn die Verarbeitung lange dauert, kann man in manchen Fällen die Unterbrechungen mit der STI-Anweisung wieder zulassen. (STI setzt den Interrupt-Indikator (IF) auf den Wert 1)
    12. Die Prozedur endet mit der Anweisung IRET, die CS, IP und Flags aus dem Stack wiederherstellt, so dass das unterbrochene Programm fortgesetzt werden kann.
    
    Hauptunterbrechungsleitungen: INTR, NMI und RESET
    INTA: eine der Klemmen, um Unterbrechungen zu verwalten
    
 2. Das Gerät gibt dem Prozessor einen Hinweis auf die Quelle des Interrupts, sodass er die richtige Routine ausführt.
    Dann wird mit diesem Hinweis auf einen Interruptvektor zugegriffen, der jedem Interrupttyp die Adresse der entsprechenden Interruptroutine zuordnet.
    
 3. a) Für das BS beobachtet man dessen Entscheidungen und Reaktionen.
    b) Bei der CPU wird darauf geachtet, ob sie einen CPU-Interrupt-Code (CPU) erhalten hat. CPU-Interrupt-Code ist ein Code, der per Software oder Hardware an eine CPU gesendet wird, um die Ausführung aller Prozesse zu unterbrechen, bis der im Interrupt angeforderte Prozess beendet ist.
    

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
