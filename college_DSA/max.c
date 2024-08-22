#include <stdio.h>

int main() {
    int arr[10];
    int i, max;

    // Input 10 numbers
    printf("Enter 10 numbers:\n");
    for (i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }

    // Initialize max with the first element
    max = arr[0];

    // Iterate through the array to find the maximum element
    for (i = 1; i < 10; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // Output the maximum element
    printf("The maximum element in the array is: %d\n", max);

    return 0;
}
