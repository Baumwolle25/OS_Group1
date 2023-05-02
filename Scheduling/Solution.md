# Gruppe 1 Lösungen Signale, Interrupts, Scheduling

## Aufgabe 1

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
