#include<bits/stdc++.h>
#include "../print.cpp"
using namespace std;

/*
  monotonic descreasing stack - Its stack with element ordered in decreasing order from bottom of stack
  we pop all smaller elements before inserting larger one.
*/


// 739. Daily Temperatures
class Solution1 {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        stack<int> st; // stores elements index
        vector<int> ans(temp.size(), 0);
        
        for(int i=0;i<temp.size(); i++) {
            while(!st.empty() && temp[st.top()] < temp[i]) {
                ans[st.top()] = i - st.top();
                st.pop();
            }
            st.push(i);
        }

        return ans;
    }
};


// 84. Largest Rectangle in Histogram
class Solution2 {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int,int>> st; // monotonic increasing stack
        int maxArea = 0;
        for(int i=0; i<heights.size(); i++) {
            int hist_count = 0;
            while(!st.empty() && heights[st.top().first] > heights[i]) {
                int area = heights[st.top().first] * (i - st.top().first + st.top().second);
                maxArea = max(maxArea, area);
                hist_count += st.top().second;
                st.pop();
                ++hist_count;
            }

            st.push({i, hist_count});
        }

        int i = heights.size();
        while(!st.empty()) {
            int area = heights[st.top().first] * (i - st.top().first + st.top().second);
            maxArea = max(maxArea, area);
            st.pop();
        }

        return maxArea;
    }
};


int main() {
  // test solution1
  vector<int> temperature = {73,74,75,71,69,72,76,73};
  vector<int> ans = Solution1().dailyTemperatures(temperature);
  cout << "ans: " << ans << endl;

  // test solution2
  vector<int> heights = {2,1,5,6,2,3};
  int maxArea = Solution2().largestRectangleArea(heights);
  cout << "maxArea: " << maxArea << endl;
}


// 30 40 50 60 30
// 30 40 50 60 