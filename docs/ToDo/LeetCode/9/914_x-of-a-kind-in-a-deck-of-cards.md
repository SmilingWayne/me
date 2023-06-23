/*In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
*/


/*
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
*/

Java.vision1: 

class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        int[] count = new int[10000];
        for(int num:deck){
            count[num]++;
        }
        int x = 0;
        for(int cnt:count){
            if(cnt > 0){
                x = gcd(x,cnt);
                if(x==1){
                    return false;
                }
            }
        }
        return x>=2;
    }
    public int gcd(int x, int y){
        return y==0?x:gcd(y,x%y);
    }
}

