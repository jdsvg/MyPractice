#include <iostream>
using namespace std;

int val(int num, int pross, string msg="Wrong amount of numbers. Start over"){
  if(pross ==1 && (num <= 0 || num > 50)){
    cout << "Only numbers. Between 1 to 50 " << endl;  
    if (num > 50) cout << msg << endl; exit(0);
  }else if(pross == 2 && (num <= 0 || num > 10*10*10)){
    cout << msg << endl; exit(0);
    cout << "No Numero" << endl;  
  }else{
    return num;
  }
}

int main() {
	int num;
  cout << "Escribe" << endl;cin >> num;
  val(num,1);
  
}