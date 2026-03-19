#include <iostream>  
#include <cmath>     
using namespace std;


bool ehPrimo(int n) {
    if (n < 2) return false; 

    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }

    return true; 
}


int main() {
    int N;

    cout << "Contador de numeros primos - by Jair" << endl;

    cout << "Digite um numero inteiro maior que zero: ";
    cin >> N;

    while (cin.fail() || N < 1) {
        cin.clear();
        cin.ignore(1000, '\n');
        cout << "Entrada invalida! Digite um numero inteiro maior que 0: ";
        cin >> N;
    }

    int quantidade = 0;

    cout << "\nN = " << N << endl;
    cout << "Primos encontrados: ";

    for (int i = 2; i <= N; i++) {
        if (ehPrimo(i)) {
            if (quantidade > 0) cout << " - ";
            cout << i;
            quantidade++;
        }
    }

    cout << "\nQuantidade de primos: " << quantidade << endl;

    cout << "\nPressione enter para sair";
    cin.ignore(1000, '\n');
    cin.get();

    return 0;
}
