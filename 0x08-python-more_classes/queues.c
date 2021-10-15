#include <stdio.h>
/**
 * sample of queue algorithm
 * 1:Check if list is full
 * 2:Check if list is empty
 * 3:Enqueue
 * ##if list is full abort else add
 * 4:Dequeue
 * ##if list is empty abort else dequeue
 */
void enqueue(int *p,int n){
    int rear = p[0];
    if (sizeof(p) == n - 1){
        printf("Overflow!");
    }
    else{
        rear = rear + 1;
    }
}
void dequeue(int *p, int n){
    int front = sizeof(p);
    if (sizeof(p) == 0){
        for (int i = 0; i <= n - 1;i++)
           p[i] = p[i - 1];
    }
    else{
        printf("Sorry there's nothing to delete!")
    }
    int main(){
        int *p;
        int a[9] = {1,2,3,4,5,6,7,8,9};
        p = a;
        int n = 9;
        enqueue(a, n);        
        return 0;
    }

