/*
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

*/

class Solution {
    public int minIncrementForUnique(int[] A) {
        Arrays.sort(A);
        int res = 0;
        if(A.length==1){
            return 0;
        }
        for(int i =1;i<A.length;i++){
            if(A[i-1]==A[i]){
                res+=1;
                A[i]+=1;
            }
            else if(A[i]<A[i-1]){
                res+=A[i-1]+1-A[i];
                A[i]=A[i-1]+1;
            }
        }
        return res;
    }
}
