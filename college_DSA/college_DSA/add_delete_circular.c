// short circular queue
/* #include <stdio.h>
#define size 5

void insertq(int[], int);
void deleteq(int[]);
void display(int[]);

int front = -1;
int rear = -1;

void insertq(int queue[], int item)
{
    if ((front == 0 && rear == size - 1) || (front == rear + 1))
    {
        printf("queue is full");
        return;
    }
    else if(rear == -1)
    {
        rear++;
        front++;
    }
    else if(rear == size - 1 && front > 0)
    {
        rear = 0;
    }
    else
    {
        rear++;
    }
    queue[rear] = item;
}

void deleteq(int queue[])
{
    if (front == -1)
    {
        printf("Queue is empty ");
    }
    else if(front == rear)
    {
        printf("\n %d deleted", queue[front]);
        front = -1;
        rear = -1;
    }
    else
    {
        printf("\n %d deleted", queue[front]);
        front++;
    }
}

void display(int queue[])
{
    int i;
    printf("\n");
    if (front > rear)
    {
        for (i = front; i < size; i++)
        {
            printf("%d ", queue[i]);
        }
        for (i = 0; i <= rear; i++)
            printf("%d ", queue[i]);
    }
    else
    {
        for (i = front; i <= rear; i++)
            printf("%d ", queue[i]);
    }
}

int main()
{
    int n, ch;
    int queue[size];
    do
    {
        printf("\n\n Circular Queue:\n1. Insert \n2. Delete\n3. Display\n0. Exit");
        printf("\nEnter Choice 0-3? : ");
        scanf("%d", &ch);
        switch (ch)
        {
        case1:
            printf("\nEnter number: ");
            scanf("%d", &n);
            insertq(queue, n);
            break;
        case2:
            deleteq(queue);
            break;
        case3:
            display(queue);
            break;
        }
    } while (ch != 0);
}*/


#include <stdio.h>
#define SIZE 5  // Define the size of the circular queue

int queue[SIZE];
int front = -1, rear = -1;

// Function to check if the queue is full
int isFull() {
    if ((front == 0 && rear == SIZE - 1) || (rear == (front - 1) % (SIZE - 1))) {
        return 1;
    }
    return 0;
}

// Function to check if the queue is empty
int isEmpty() {
    if (front == -1) {
        return 1;
    }
    return 0;
}

// Function to add an element to the circular queue
void enqueue(int value) {
    if (isFull()) {
        printf("Queue is Full!\n");
        return;
    } else {
        if (front == -1)  // First element insertion
            front = 0;
        rear = (rear + 1) % SIZE;
        queue[rear] = value;
        printf("%d added to the queue.\n", value);
    }
}

// Function to delete an element from the circular queue
int dequeue() {
    if (isEmpty()) {
        printf("Queue is Empty!\n");
        return -1;
    }
    int data = queue[front];
    if (front == rear) {  // Queue has only one element
        front = -1;
        rear = -1;
    } else {
        front = (front + 1) % SIZE;
    }
    return data;
}

// Function to display the elements in the circular queue
void display() {
    if (isEmpty()) {
        printf("Queue is Empty!\n");
        return;
    }
    printf("Queue elements are: ");
    int i = front;
    while (i != rear) {
        printf("%d ", queue[i]);
        i = (i + 1) % SIZE;
    }
    printf("%d\n", queue[rear]);
}

int main() {
    int choice, value;

    while (1) {
        printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the value to be added: ");
                scanf("%d", &value);
                enqueue(value);
                break;
            case 2:
                value = dequeue();
                if (value != -1)
                    printf("%d dequeued from the queue.\n", value);
                break;
            case 3:
                display();
                break;
            case 4:
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}
