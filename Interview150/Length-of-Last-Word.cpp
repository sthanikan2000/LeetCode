// Problem can be solved using python with return len(s.rstrip().split()[-1])
// But this solution is for the languages don't have rstrip, split
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len=s.length();
        int i = 0;
        int j = 0;
        while (len-i>0 && s[len-1-i] == ' '){
            j++;
            i++;
        }
        // cout<< j;
        while (len-i>0 && s[len-1-i] != ' '){
            i++;
        }
        return i-j;
        
    }
};