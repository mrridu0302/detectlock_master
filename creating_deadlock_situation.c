#include <stdio.h> 
#include<unistd.h> 
#include <pthread.h>

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER;
void thread1_function() {
    printf("Thread 1: Attempting to lock mutex1...\n");
    pthread_mutex_lock( & mutex1);
    printf("Thread 1: Locked mutex1.\n");
    // Sleep to simulate some work being done sleep(2);
    printf("Thread 1: Attempting to lock mutex2...\n");
    pthread_mutex_lock( & mutex2);
    printf("Thread 1: Locked mutex2.\n");
    // Perform some critical section work here
    pthread_mutex_unlock( & mutex2);
    printf("Thread 1: Unlocked mutex2.\n");
    pthread_mutex_unlock( & mutex1);
    printf("Thread 1: Unlocked mutex1.\n");
    //return NULL; }
    void thread2_function() {
        printf("Thread 2: Attempting to lock mutex2...\n");
        pthread_mutex_lock( & mutex2);
        printf("Thread 2: Locked mutex2.\n");
        // Sleep to simulate some work being done sleep(2);
        printf("Thread 2: Attempting to lock mutex1...\n");
        pthread_mutex_lock( & mutex1);
        printf("Thread 2: Locked mutex1.\n");
        // Perform some critical section work here
        pthread_mutex_unlock( & mutex1);
        printf("Thread 2: Unlocked mutex1.\n");
        pthread_mutex_unlock( & mutex2);
        printf("Thread 2: Unlocked mutex2.\n");
        // return NULL; }
        int main() {
          pthread_t thread1, thread2;
          // Create two threads
          pthread_create( & thread1, NULL, thread1_function, NULL);
          pthread_create( & thread2, NULL, thread2_function, NULL);
          // Wait for the threads to finish pthread_join(thread1, NULL); pthread_join(thread2, NULL);
          return 0;
        }
