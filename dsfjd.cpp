// Write a program to count positive and negative numbers
#include <iostream> // Include input and output 
using namespace std; // Use the stadard namespace (No need for std:)
 
int main(){ 

    // Create integers array
    int arr[] = {-3 , -2 , 0 , -5 , -4 , 9, 7 , 6};

    // These will count how many positive and negative numbers
    int positive = 0 , negative = 0;
    
    // Outer loop go through each number
    for (int i = 0 ; i < 8 ; i++){

        // If 0 skip
        if (arr[i] == 0)
            continue;
        // If the num is > 0 positive
        if (arr[i] > 0)
            positive++ ;//Add 1 to positive count
        // If the num is < 0 negative
        else
            negative++;//Add 1 to negative count
            
    }

    //Show how much numbers
    cout << "Positive Num: " << positive <<endl;
    cout << "Negative Num: " << negative <<endl;
 
    return 0; // end program
} 

