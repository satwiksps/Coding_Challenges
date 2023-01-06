#include <iostream>
using namespace std;

int main() {
    int num = 1234, rev = 0;
    while (num != 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    cout << "Reversed Number: " << rev;
    return 0;
}
