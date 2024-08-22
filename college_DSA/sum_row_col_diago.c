#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter the size of the matrix (n x n): ");
    scanf("%d", &n);

    int matrix[n][n];
    int rowSum[n], colSum[n], mainDiagSum = 0, antiDiagSum = 0;

    // Initialize sums to 0
    for (i = 0; i < n; i++) {
        rowSum[i] = 0;
        colSum[i] = 0;
    }

    // Input the matrix
    printf("Enter the elements of the matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Calculate the sum of rows, columns, and diagonals
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            rowSum[i] += matrix[i][j];
            colSum[j] += matrix[i][j];
            if (i == j) {
                mainDiagSum += matrix[i][j]; // Main diagonal
            }
            if (i + j == n - 1) {
                antiDiagSum += matrix[i][j]; // Anti diagonal
            }
        }
    }

    // Output the results
    printf("\nSum of rows:\n");
    for (i = 0; i < n; i++) {
        printf("Row %d: %d\n", i + 1, rowSum[i]);
    }

    printf("\nSum of columns:\n");
    for (i = 0; i < n; i++) {
        printf("Column %d: %d\n", i + 1, colSum[i]);
    }

    printf("\nSum of main diagonal: %d\n", mainDiagSum);
    printf("Sum of anti diagonal: %d\n", antiDiagSum);

    return 0;
}
