#include <map>
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> mag;
        // cout << mag.size();
        for (auto &ch : magazine) { 
            mag[ch]++;
        } 
        for (auto &ch : ransomNote){
            if (mag[ch] == 0) return false;
            mag[ch]--;
        }
        return true;
        
    }
};