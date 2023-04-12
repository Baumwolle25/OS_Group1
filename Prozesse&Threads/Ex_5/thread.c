// Kompilation : gcc -o Aufgabe5 -pthread thread.c
//Ausführung : ./Aufgabe5 100
//sourcen : https://franckh.developpez.com/tutoriels/posix/pthreads/#LIV-A

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>

int sum=0;                          //Die gloabale Variable
pthread_mutex_t mutex;

void * helloworld(void * arg) {         //Die Funktion, dass jeder thread 1.000.000 mal eine Schleife durchlaufen
    int argument = * (int*)arg;
    for (int i = 0; i < 1000000; i++)
    {
        pthread_mutex_lock(&mutex);
        sum+= argument;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int argc, char** argv){    
    int i, zh;                     
    int * args;
    pthread_t * threads;
    zh = atoi(argv[1]);
    threads = malloc(zh * sizeof(pthread_t));
    args = malloc(zh * sizeof(int));
    pthread_mutex_init(&mutex, NULL);           //initalisierung der mutex
    for (i = 0; i < zh; i++) {
        int var=0;
        if (i%2==0){                             //die Hälfte addieren in einer Schleife 5 Mal jeweils eine 1 
            for (int j = 0; j < 5; j++)
            {
                var+=1;
            }
            
        }
        else{                                   //die Hälfte subtrahieren in einer Schleife 5 Mal jeweils eine 1 
            for (int j = 0; j < 5; j++)
            {
                var-=1;
            }
        }

        args[i] = var;
        pthread_create(&threads[i], NULL, helloworld, &args[i]);   //Erzeugung den Threads
    }

    for (i = 0; i < zh; i++) {
        pthread_join(threads[i], NULL);                 //Sammeleung alle Threads
        printf("thread Nr. %d joined \n", i);
    }
    printf("Summe=%d\n",sum);
    return 0;
}
