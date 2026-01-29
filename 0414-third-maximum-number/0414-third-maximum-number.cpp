class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> mySet;
        for (int num : nums) {
            mySet.insert(num);
        }

        int idx = mySet.size() - 3;
        int maxElement = *mySet.rbegin();

        if (idx >= 0 && idx < mySet.size()) {
            set<int>::iterator it = mySet.begin();
            advance(it, idx);
            return *it;
        } else {
            return maxElement;
        }
    }
};
