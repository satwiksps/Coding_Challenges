#include <iostream>
using namespace std;

// Function to print Fibonacci sequence up to n terms
void fibonacci(int n) {
    int t1 = 0, t2 = 1, nextTerm = 0;
    cout << "Fibonacci Sequence: ";
    for (int i = 1; i <= n; ++i) {
        cout << t1 << " ";
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter number of terms: ";
    cin >> n;
    fibonacci(n);
    return 0;
}