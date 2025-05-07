#include <iostream>
using namespace std;
int main(){
    int k;

    cout << "Digite um numero inteiro de 1 a 10:\n";
    cin >> k;
    cout << "O numero que voce digitou: "<< k << endl;

    cout << "Contagem:\n";
    for(int i = 0; i <= k; i++){
        cout << i << endl;
    }
}