class Solution {
public:
    char findTheDifference(string s, string t) {
        
        char c = 0;
        
        for( int i = 0; i < s.size(); i++)
            c = c^s[i];
        
        for( int j = 0; j < t.size(); j++)
            c = c^t[j];
        
        return c;
        
    }
};

T: O(n)
    
Logic
1. XOR is the best solution to find the odd element out becasue 1^1 = 0 and 1^0 = 1
2. XOR all the element of both the string we will get the odd element out.