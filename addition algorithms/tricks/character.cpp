#include<bits/stdc++.h>
#include "../../print.cpp"
using namespace std;


// character are internally represented using number


// 125. Valid Palindrome
class Solution {
public:
    bool isPalindrome(string s) {
        int l=0, r=s.size()-1;
        while(l<r) {
          if(!isAlpha(s[l])) ++l;
          else if(!isAlpha(s[r])) --r;
          else if(toSmall(s[l])!=toSmall(s[r])) 
            return false;
          else ++l, --r;
        }
        return true;
    }

    bool isAlpha(char c) { // a-z or A-Z or 0-9
      return (c>='a' && c <='z') || (c>='A' && c<='Z') || (c>='0' && c<='9');
    }
    char toSmall(char c) { // if A-Z then a-z else same char
      return (c>='A' && c<='Z') ? c + 32 : c;
    }
};

int main() {
  bool result = Solution().isPalindrome("A man, a plan, a canal: Panama");
  cout << result << endl;
  return 0;
}
