#include <iostream>
using namespace std;
// This is my first c++ program 
    char myVar = 'A';
    char myFunction (){
        char  myVar = 'B';
        return myVar;
    }
int main(){
    cout << "Function call:" << myFunction() << endl;
    cout << "Value of myVar:" << myVar << endl;
    myVar = 'z';
    cout << "Functioon call:" << myFunction() << endl;
    cout << "Value of myVar:" << myVar << endl;
    return 0; 
}