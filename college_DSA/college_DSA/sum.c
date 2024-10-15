#include <stdio.h>
int main()
{
    int number[10];
    int sum = 0;
    printf("enter 10 number is:\n ");
    for (int i = 0; i < 10; i++)
    {
        printf("number %d:", i + 1);
        scanf("%d", &number[i]);
        sum = sum + number[i];
    };
    printf("the sum of thr 10 number is:%d\n", sum);
    return 0;
}
