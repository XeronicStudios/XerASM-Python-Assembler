#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    __asm__(
        "movl %edx, %eax\n\t" 
        "addl $2, %eax\n\t"
    );
    return 0;
}