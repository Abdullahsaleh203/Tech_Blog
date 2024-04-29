#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <cs50.h>
// linear search 
// linear search function definition
// # Hashing 
// int* linear_search(int arr[],
//                    int n,
//                    int size)
// {
//     for (int i = 0; i < size; i++)
//     {
//         if (arr[i] == n)
//         {
//             return &arr[i];
//         }
//     }
//     return NULL;
// }
// main function definition

int main(){
    char m[
        
    ] = {"string", "hjhj"};
    int number[] = {20,
                    30,
                    50,
                    70,
                    100,
                    300};
    int n;
    int size = sizeof(number) / sizeof(number[0]); // Calculate the size of the number array
    printf("choose number: ");
    scanf("%d", &n);
    for (int i = 0; i < size; i++) // Use the size variable in the loop condition
    {
        if (number[i]==n)
        {
            printf("number is found\n");
            return 0;
        }
    }
    printf("number is not found\n");
    return 1;
};
