#include <stdio.h>

int main() {
    int rows = 3;
    int cols = 4;

    // Declare a 2D array
    int arr[3][4];

    // Initialize the 2D array with values
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            arr[i][j] = (i + 1) * (j + 1);
        }
    }

    // Print the 2D array
    printf("The 2D array is:\n");
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
