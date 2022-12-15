#include <bits/stdc++.h>
#include "../../print.cpp"
using namespace std;

// seive method: use to get all prime number less than N
vector<int> getAllPrimeNumbers(int N) {
  vector<int> isPrime(N+1, true);
  isPrime[0] = isPrime[1] = false;
  for(int i=2; i<=N; i++) {
    if(isPrime[i]) for(int n=i*2; n<=N; n+=i) isPrime[n] = false;
  }
  vector<int> ans;
  for(int i=2; i<=N; i++) {
    if(isPrime[i]) ans.push_back(i);
  }
  return ans;
}


int main() {
  vector<int> prime_numbers = getAllPrimeNumbers(1000000000);
  //cout << prime_numbers << endl;
  cout << "length of prime_numbers: " << prime_numbers.size() << endl;
  return 0;
}

