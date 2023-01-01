
#include <iostream>
using namespace std;

int main() {
    int rows, cols;
    cout << "Enter the number of rows and columns: ";
    cin >> rows >> cols;

    int mat1[rows][cols], mat2[rows][cols], result[rows][cols];

    cout << "Enter elements of the first matrix:\n";
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> mat1[i][j];

    cout << "Enter elements of the second matrix:\n";
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> mat2[i][j];

    cout << "Sum of matrices:\n";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = mat1[i][j] + mat2[i][j];
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
