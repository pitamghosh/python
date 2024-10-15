#include <stdio.h>

int main() {
    int arr[10];
    int i;

    // Input 10 numbers
    printf("Enter 10 numbers:\n");
    for (i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }

    // Print the squares of the elements
    printf("Squares of the elements:\n");
    for (i = 0; i < 10; i++) {
        printf("%d ", arr[i] * arr[i]);
    }

    printf("\n");
    return 0;
}
