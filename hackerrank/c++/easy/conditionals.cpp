#include <bits/stdc++.h>

using namespace std;



int main()
{   
    // declare integer to iterate
    int n;
    // read from input
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    // declare a string map
    string map[10] = {"one","two","three","four","five",
                        "six","seven","eight","nine","Greater than 9"};

    //check if n is greater than 9
    if (n > 9){
        cout << map[9] << endl;
    }
    // else if n is between 1 and 9
    else if (n >= 1 && n <= 9){
        cout << map[n-1] << endl;
    }
    

    return 0;
}
