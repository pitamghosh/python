#include <stdio.h>
int main()
{
    int rows, cols, i, j;
    printf("the number of rows is:");
    scanf("%d", &rows);
    printf("enter number of columns is:");
    scanf("%d", &cols);

    int arr[rows][cols];
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < cols; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    int sum_rows=0;
    int max_sum = 0;
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < cols; j++)
        {
            sum_rows = sum_rows + arr[i][j];
        }
        if (max_sum < sum_rows)
        {
            max_sum = sum_rows;
        }
    }

    int sum_cols=0;
  
    for (j = 0; j < rows; j++)
    {
        for (i = 0; i < cols; i++)
        {
            sum_cols = sum_cols + arr[i][j];
        }
        if (max_sum < sum_cols)
        {
            max_sum = sum_cols;
        }
    }
    printf("The maximum value from the sum of rows and columns is: %d\n", max_sum);
    return 0;
}
