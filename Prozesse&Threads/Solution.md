# Gruppe 1 Lösungen Einarbeitung

## Augabe 1

> fork

src: https://www.man7.org/linux/man-pages/man2/fork.2.html

Das Kommando `fork` erstellt einen `Child` Thread, der zum Zeitpunkt des Erstellens mit seinem `Parrent` bis auf die `Process ID` und eine Reihe anderer Faktoren identisch ist.

>  execl

src: https://man7.org/linux/man-pages/man3/exec.3.html

Die `exec()` Funktions-Familie erstellt ein neues `Process Image` im laufenden Prozess, wobei `execl` von `execve` erbt und `const char *arg` als Argumente für die aufzurufende Funktion annimt, die `pointer` zu `null-terminated strings` sein müssen.

> waitpid

src: https://man7.org/linux/man-pages/man2/wait.2.html

Das `waitpid` Kommando pausiert die Ausführung des aktuellen Threads bis der/die durch die `pid` spezifizierte `child` Thread/s seinen Zustand ändern.

> clone




## Augabe 2

## Aufgabe 3

> blocked -> running

Wenn ein Thread vom OS geblocked wird, wählt das OS einen anderen Thread, der ausgeführt wird. Das bedeutet, ein `blocked` Thread wird von Definiton aus nach Auflösung des `blocked` Grundes in den `ready` Zustand gesetzt um dem neuen laufenden Thread nicht zu schaden.

> ready -> blocked

Das OS blockiert einen Thread, wenn während der Laufzeit etwas passiert, auf das der Thread warten muss. Da ein Thread im `ready` Zustand auch inaktiv ist und blockert werden kann wenn das OS den Thread auswählt, braucht es eine Zustandsänderung `ready -> blocked` nicht, das ein System ordungsgemäß funktioniert.

## Aufgabe 4

## Aufgabe 5

Abgaben von Anton Stimmer, Oscar Röth