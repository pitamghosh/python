#include <stdio.h>

int main() {
    int arr[10];
    int i;

    // Input 10 numbers
    printf("Enter 10 numbers:\n");
    for (i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }

    // Print numbers in reverse order
    printf("Numbers in reverse order:\n");
    for (i = 9; i >= 0; i--) {
        printf("%d ", arr[i]);
    }

    printf("\n");
    return 0;
}
