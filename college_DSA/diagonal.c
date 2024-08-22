#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter the size of the matrix (n x n): ");
    scanf("%d", &n);

    int matrix[n][n];

    // Input the matrix
    printf("Enter the elements of the matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Print the main diagonal elements
    printf("\nMain diagonal elements:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", matrix[i][i]);
    }

    // Print the anti-diagonal elements
    printf("\n\nAnti diagonal elements:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", matrix[i][n - i - 1]);
    }

    return 0;
}
 