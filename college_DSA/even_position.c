#include <stdio.h>
int main()
{
    int row, cols;
    printf("enter row number:");
    scanf("%d", &row);
    printf("enter column number:");
    scanf("%d", &cols);

    int r[row][cols];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            scanf("%d", &r[i][j]);
        }
    }

    for (int i = 0; i < row; i = i + 2)
    {
        for (int j = 0; j < cols; j = j + 2)
        {
            printf("Even position are:%d", r[i][j]);
        }
    }
    return 0;
}