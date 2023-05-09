#aufruf:python3 Aufgabe.py 6 1 2  #6=# Anzahl der Threads; 1:Die Lesezeit; 2:# Anzahl der Schleifendurchläufe pro Thread

import threading
import time
import random
import sys

# Initialisiere Semaphore für jedes Buch
book1_sem = threading.Semaphore(3)
book2_sem = threading.Semaphore(5)
book3_sem = threading.Semaphore(4)
book4_sem = threading.Semaphore(2)

# Initialisierung die Buchzählern
zaehler_buch1 = 0
zaehler_buch2 = 0
zaehler_buch3 = 0
zaehler_buch4 = 0
students_with_three_books = 0

lhre=[]
stu=[]
# Funktion zum Ausleihen von Büchern
def borrow_books(student_id):

    global students_with_three_books
    # Wähle zufällig eine der beiden Buchkombinationen aus
    book_set = random.choice([(book1_sem, book2_sem, book3_sem), (book2_sem, book3_sem, book4_sem)])

    # Versuche, die Semaphoren für jedes Buch in der ausgewählten Kombination zu sperren
    for book_sem in book_set:
        book_sem.acquire()

    


    #print("before liehen",students_with_three_books)
    students_with_three_books+=1
    lhre.append(students_with_three_books)
    stu.append(student_id)
   # print("after liehen",students_with_three_books)
    #print(f"longueurlh={len(lhre)}")
    print(f"Student {student_id} hat Bücher ausgeliehen und {lhre[-1]} {lhre} Lange={len(lhre)} Sutdent-en hat/haben 3 Bücher")

    # Wartezeit zum Lesen der Bücher
    time.sleep(WAIT_TIME)

    # Gib die Bücher zurück, indem du die Semaphoren freigibst

    for book_sem in book_set:
        book_sem.release()
    #print("before release",students_with_three_books)
    students_with_three_books-=1
    lhre.append(students_with_three_books)
    stu.append(student_id)
    #print(f"after release {students_with_three_books}")

    #print(f"longueurlh={len(lhre)}")
    print(f"Student {student_id} hat Bücher zurückgegeben und {lhre[-1]} {lhre} Lange={len(lhre)} Sutdent-en hat/haben 3 Bücher")



# Anzahl der Threads
num_threads = int(sys.argv[1])

# Wartezeit für das Lesen der Bücher
WAIT_TIME = int(sys.argv[2])

# Anzahl der Schleifendurchläufe pro Thread
num_iterations = int(sys.argv[3])

# Erstelle Threads
threads = []
for i in range(num_threads):
    t = threading.Thread(target=borrow_books, args=(i+1,))
    threads.append(t)

# Starte Threads
for t in threads:
    t.start()
    
# Warte auf Threads
for t in threads:
    t.join()

#for i in range(len(lhre)):
#    print(f"Student {stu[i]} hat Bücher zurückgegeben und {lhre[i]} Sutdent-en hat/haben 3 Bücher")
print(f"lhre={lhre}")
print(f"stu={stu}")
