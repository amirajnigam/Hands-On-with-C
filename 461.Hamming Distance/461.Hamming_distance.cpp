class Solution {
public:
    
    int set_bits(int n)
    {
        int count = 0;
        while(n){
            if(n & 1 == 1)
                count++;
            n = n>>1;
        }    
        return count;
    }
    
    int hammingDistance(int x, int y) {
        int n = x ^ y;
        return (set_bits(n));
        
    }
    
    //Alternat Approach
    //     int hammingDistance(int x, int y) {
    //     return bitset<32>(x^y).count();
    // }
};

T: O(n)

Logic
1. XOR both the numbers
2. we will get 1 for different number
3. Calculate set bit in XORed number