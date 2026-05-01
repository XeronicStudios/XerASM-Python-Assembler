#include <stdio.h>
#include <stdlib.h>

int LDR(int Destination, int Source) {
    asm volatile (
        "movl %[dt], %[src]" 
        : [dt] "=r" (Destination) 
        : [src] "r" (Source)  
    );
    printf("Return: %i\n", Destination);
    return 0;
};

int STR(int Destination, int Source) {
    asm volatile (
        "movl %[src], %[dt]" 
        : [dt] "=r" (Destination) 
        : [src] "r" (Source)  
    );
    printf("Return: %i\n", Destination);
    return 0;
};

int ADD(int Destination, int Source) {
    asm volatile (
        "add %[src], %[dt]"
        : [dt] "+r" (Destination)
        : [src] "r" (Source)
    );
    printf("Return: %i\n", Destination);
    return 0;
};

int SUB(int Destination, int Source) {
    asm volatile (
        "sub %[src], %[dt]"
        : [dt] "+r" (Destination)
        : [src] "r" (Source)
    );
    printf("Add: %i\n", Destination);
    return 0;
};

//int CMP(int Destination, int Source) {
//    asm volatile (
//        ""
//    );
//};

int AND(int Destination, int Source) {
    for (int i = 0; i < 5; i++) {
        printf("Iteration\n");
    };
    asm volatile (
    "add %[dst], %[src]"
    : [dst] "=r" (Destination) 
    : [src] "r" (Source));
    printf("Return: %i\n", Destination);
    return 0;
}

int main() {
    AND(0010, 1110);
    exit;
    return 0;
}

//int main() {
//    int a = 5, b = 5, sum;

    // Extended inline assembly (GCC/Clang)
//]    asm volatile (
//        "addl %[val_b], %[val_a]"   // sum = a + b
//        : [val_a] "+r" (a)          // output: a is updated in-place
//        : [val_b] "r" (b)           // input: b is read-only
//    );

//    sum = a; // a now contains the sum
//    printf("Sum = %d\n", sum);

//    return 0;
//}