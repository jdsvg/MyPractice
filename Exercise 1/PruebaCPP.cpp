#include <iostream>
#include <string>
#include <sstream>
using namespace std;

void val(int num, int pross){
  string num_str ="";
  string pross_str ="";
  try{
    num = stoi(num_str);
    cout << "Es un numero" << endl;
  }catch(...){
    cout << "No es un numero" << endl;
  }
  cout << 2*2 << endl;
}

int main() {
	int num;
  cout << "Escribe" << endl;
	cin >> num;    //Reading input from STDIN
	cout << "Input number is " << num << endl;	// Writing output to STDOUT
cout << typeid(<object>).name() << endl;
  //val(1,2);
}