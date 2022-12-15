#include<bits/stdc++.h>
using namespace std;


/*
  map<char,int> & set<char> can be implemented using array of size of charset
*/


int main() {
  string a = "abcdsdab";

  // dictionary using map
  map<char,int> mp;
  for(char ch: a) ++mp[ch];

  // ** more efficient when input is very big
  // dictionary using vector
  vector<int> v(26, 0); // a-z contains 26 characters
  for(char ch: a) ++v[ch-'a'];
  

  for(int i=0; i<26; ++i) if(v[i]!=0) cout << char(i+'a') << ":" << v[i] << ", ";
}