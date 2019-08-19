#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
  int array[] = { 10, 20};
  int *p = array;
  cout << p << '\t' << "*p =" << *p << endl;
  int v = *p++;
  printf("v = %d, array[0] = %d, array[1] = %d, *p = %d\n", 
  v, array[0], array[1], *p);
  cout << p << endl;
  return 0;
}