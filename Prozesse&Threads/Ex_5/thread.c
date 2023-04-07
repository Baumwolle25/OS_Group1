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
    int ordre = * (int*)arg;
    for (int i = 0; i < 1000000; i++)
    {
        pthread_mutex_lock(&mutex);
        sum+= ordre;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int argc, char** argv){    
    int i, nb, var;                     
    int * args;
    pthread_t * threads;
    nb = atoi(argv[1]);
    threads = malloc(nb * sizeof(pthread_t));
    args = malloc(nb * sizeof(int));
    pthread_mutex_init(&mutex, NULL);           //initalisierung der mutex
    for (i = 0; i < nb; i++) {
        if (i%2==0)                             //die Hälfte addieren in einer Schleife 5 Mal jeweils eine 1 
            {var=5*1;}
        else
            {var=-(5*1);}                       //die Hälfte addieren in einer Schleife 5 Mal jeweils eine 1 
        
        args[i] = var;
        pthread_create(&threads[i], NULL, helloworld, &args[i]);   //Erzeugung den Threads
    }
    for (i = 0; i < nb; i++) {
        pthread_join(threads[i], NULL);                 //Sammeleung alle Threads
        printf("thread Nr. %d joined \n", i);
    }
    printf("Summe=%d\n",sum);
    return 0;
}