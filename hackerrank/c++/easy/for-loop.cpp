#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // declare integers
    int start, end;
    
    // declare a string map to print numbers
    string map[9]= {"one","two","three","four","five","six","seven","eight","nine"};
    
    // read in the start and end 
    cin >> start >> end;

    // iterate from the start to the end
    for (int i = start; i <= end; i++){
        // if the current value is between 1 and 9
        if (i >= 1 && i <= 9){
            cout << map[i-1] << endl;
        }
        // else if the value is greater than 9
        else if (i > 9){
            // if the value is even
            if (i % 2 == 0){
                cout << "even" << endl;
            }
            // else if the value is odd
            else{
                cout << "odd" << endl;
            }
        }
    }
    return 0;
}
