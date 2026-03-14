#include <stdio.h>

int testcall(int Val) {
    int x = Val;
    int y = x + 1;
    return y;
};

int LDR(int Val1, int Val2) {
    int Result;
    asm volatile (
        "lea 100(%[reg_a]), %[reg_b]"
        : [reg_a] "+r" (Val1)
        : [reg_b] "r" (Val2)
    );
    printf("Result: %i", Val2);
    return 0;
};

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