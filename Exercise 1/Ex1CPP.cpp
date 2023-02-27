#include <iostream>
using namespace std;

int myFun(){
  return 2*2;
}

int main() {
	int num;
  cout << "Escribe" << endl;
	cin >> num;    //Reading input from STDIN
	cout << "Input number is " << num << endl;	// Writing output to STDOUT

  myFun();
}