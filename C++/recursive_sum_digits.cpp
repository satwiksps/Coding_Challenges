#include <iostream>
using namespace std;

int sumDigits(int n) {
    if (n == 0) return 0;
    return n % 10 + sumDigits(n / 10);
}

int main() {
    cout << "Sum of digits: " << sumDigits(1234);
    return 0;
}