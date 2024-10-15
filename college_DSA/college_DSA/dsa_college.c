#include <stdio.h>

#include <stdlib.h>
#include <string.h>

int evaluatePrefix(char *prefix)
{
    int stack[100];
    int top = -1;
    int i;

    for (i = strlen(prefix) - 1; i >= 0; i--)
    {
        if (prefix[i] >= '0' && prefix[i] <= '9')
        {
            // Push operand to stack
            stack[++top] = prefix[i] - '0';
        }
        else
        {
            // Pop two operands from stack and apply operator
            int operand2 = stack[top--];
            int operand1 = stack[top--];
            switch (prefix[i])
            {
            case '+':
                stack[++top] = operand1 + operand2;
                break;
            case '-':
                stack[++top] = operand1 - operand2;
                break;
            case '*':
                stack[++top] = operand1 * operand2;
                break;
            case '/':
                stack[++top] = operand1 / operand2;
                break;
            }
        }
    }

    // Return the final result
    return stack[top];
}

// Function to evaluate postfix expression
int evaluatePostfix(char *postfix)
{
    int stack[100];
    int top = -1;
    int i;

    // Traverse the postfix expression from left to right
    for (i = 0; i < strlen(postfix); i++)
    {
        if (postfix[i] >= '0' && postfix[i] <= '9')
        {
            // Push operand to stack
            stack[++top] = postfix[i] - '0';
        }
        else
        {
            // Pop two operands from stack and apply operator
            int operand2 = stack[top--];
            int operand1 = stack[top--];
            switch (postfix[i])
            {
            case '+':
                stack[++top] = operand1 + operand2;
                break;
            case '-':
                stack[++top] = operand1 - operand2;
                break;
            case '*':
                stack[++top] = operand1 * operand2;
                break;
            case '/':
                stack[++top] = operand1 / operand2;
                break;
            }
        }
    }

    // Return the final result
    return stack[top];
}

int main()
{
    char prefix[100], postfix[100];

    printf("Enter prefix expression: ");
    scanf("%s", prefix);
    printf("Result: %d\n", evaluatePrefix(prefix));

    printf("Enter postfix expression: ");
    scanf("%s", postfix);
    printf("Result: %d\n", evaluatePostfix(postfix));

    return 0;
} 

