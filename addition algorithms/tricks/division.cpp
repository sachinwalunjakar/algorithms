#include <bits/stdc++.h>
#include "../../print.cpp"
using namespace std;

/*
  trick : use division to store two number at each position in array
    1. as quotient
    2. as remainder
*/

// gfg: Rearrange Array Alternately
class Solution {
  public:
  vector<int> reArrange(vector<int> array) {
    int max_element = array[array.size()-1] + 1;
    int min_index = 0, max_index = array.size()-1;
    for(int i=0; i<array.size(); ++i) {
      if(i%2==0) {
        array[i] += (array[max_index] % max_element) * max_element;
        --max_index;
      }
      else {
        array[i] += (array[min_index] % max_element) * max_element;
        ++min_index;
      }
    }

    for(int i=0; i<array.size(); ++i) array[i] /= max_element;

    return array;
  }
};

int main() {
  vector<int> output = Solution().reArrange({1,2,3,4,5,6,7,8});
  cout << output << endl;
  return 0;
}