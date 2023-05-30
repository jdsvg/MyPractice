#include <iostream>
#include <typeinfo>
using namespace std;

int val(int num, int pross, string msg="Wrong amount of numbers. Start over"){
  if(pross == 1 && (num <= 0 || num > 50)){
    cout << "Only numbers. Between 1 to 50 " << endl;
    cout << msg << endl; exit(0);
  }else if(pross == 2 && (num <= 0 || num > 10*10*10)){
    cout << "Only numbers. Between 1 to 1000" << endl;
    cout << msg << endl; exit(0);
  }else{
    return num;
  }
}

int* fillArray(int size) {
    int num = 0;
    int* newArr = new int[size];
    for (int i = 0; i < size; i++) {
      cout << "Enter the number for "<<i+1<<" position"<<endl;
      cin >> num;      
      val(num, 2);
      newArr[i] = num;
    }
    return newArr;
}

int* sortedArray(int* unsortedArray, int size){
  int aux = 0;
   for(int i = 0; i<size; i++){
     for(int j = i+1; j<size; j++){ 
      if(unsortedArray[i]<unsortedArray[j]){
        aux = unsortedArray[i];unsortedArray[i] = unsortedArray[j];unsortedArray[j] = aux;
      }
     }
   }
  return unsortedArray;
}

int* gcd(int* array){
  int* gcdArr = new int[1];
  int divisor=0, divisor_one = 0, dividend=0, dividend_one = 0, remainder=0, gcd = array[0], size = sizeof(array)/sizeof(array[0]); 
  
  for (int i = 1; i<=size; i++){
    divisor = gcd;dividend = array[i];remainder = dividend % divisor;
      if(remainder == 0){
        gcd = divisor;
      }else{
        while(remainder != 0){
          dividend_one = divisor;divisor_one = remainder;remainder = dividend_one % divisor_one;gcd = divisor_one;
        }
      }
  }
  gcdArr[0] = gcd; 
  return gcdArr;
}

int power(int a, int b){
  int r=a;
  while(b>1){
    r*=a;
    b--;
  }
  return r;
}

int main() {
	int num;
  cout << "Enter the amount of numbers" << endl;cin >> num;
  val(num,1);
  int* newArr = fillArray(num);
  newArr = sortedArray(newArr, num);
  int xgcd = gcd(newArr)[0], x = 1;
  
  for(int i = 0; i < num; i++)x*=newArr[i];

  std::cout << "GCD: " << power(x,xgcd) << endl;
}