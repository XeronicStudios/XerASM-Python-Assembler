#include <stdio.h>

int main() {
    int a = 0;
    int b = 5;
    __asm__(
        "movl $4, %0" 
        : "=r" (a)
    );
    printf("Test %i", a);
    return 0;
}