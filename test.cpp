#include <bits/stdc++.h>
#include "print.cpp"
using namespace std;




int main() {
  vector<int> a = {1,2};
  int total = 0;
  for(int i=0; i<a.size(); i++) {
    total += a[i];
  }
  cout << "total: " << total << endl;
  return 0;
}