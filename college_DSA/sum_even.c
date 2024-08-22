#include<stdio.h>
int main()
{
    int row,col;
    printf("enter any rows:");
    scanf("%d",&row);
    printf("enter any columns");
    scanf("%d",&col);

    int arr[row][col];

    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    int sum=0;
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            if(arr[i][j]%2==0)
            {
                sum=sum+arr[i][j];
            }
        }
    }
    printf("the sum of the even number is:%d\n",sum);
    return 0;

}