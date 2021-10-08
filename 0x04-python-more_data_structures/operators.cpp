#include <iostream>
using namespace std;
//swapping the values of two variables
int main(){
    int a = 50;
    int b = 30;
    int temp;
    cout << "Value for a:" << a << endl;
    cout << "Value for b:" << b << endl <<endl;
    temp = b;
    b = a;
    a = temp;
    cout << "==After Swap=="<<endl <<endl;
    cout << "Value for a:" << a <<endl;
    cout << "Value for b:" << b << endl;
    return 0;
}
