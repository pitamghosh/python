#include <stdio.h>

int main()
{
    int numbers[10];
    int sum = 0;
    float average;

    // Prompting the user to input 200 numbers
    printf("Enter 10 numbers:\n");
    for (int i = 0; i < 10; i++)
    {
        printf("Number %d: ", i + 1);
        scanf("%d", &numbers[i]);
        sum = sum + numbers[i]; // Adding each number to sum
    }

    // Calculating the average
    average = sum / 10;

    // Displaying the average
    printf("The average of the 10 numbers is: %.2f\n", average);

    return 0;
}