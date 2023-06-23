/*给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 *-1。

你可以认为每种硬币的数量是无限的。
*/

BFS：

class Solution {
    
    public int coinChange(int[] coins, int amount) {
        if(amount == 0){
            return 0;
        }
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> map = new HashSet<>();
        queue.offer(amount);
        int cnt = 0 ;
        while(queue.size()!= 0){
            cnt ++;
            int size = queue.size();
            for(int j = 0 ; j < size; j ++ ){
                int target = queue.poll();
                for(int i = 0; i < coins.length; i ++ ){
                    if(target - coins[i] == 0){
                        return cnt;
                    }
                    else{
                        if(target - coins[i] > 0){
                            if(map.contains(target - coins[i])){
                                continue;
                            }
                            else{
                                map.add(target - coins[i]);
                                queue.offer(target - coins[i]);
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
}

DFS 
class Solution {
    int minCount = Integer.MAX_VALUE;
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        recursion(coins, amount, 0, coins.length - 1);
        return minCount == Integer.MAX_VALUE ? -1 : minCount;
    }
    

    public void recursion(int[] coins, int amount, int count, int index) {
        if (index < 0 || count + amount / coins[index] >= minCount) return;
        if (amount % coins[index] == 0) {
            minCount = Math.min(minCount, count + amount / coins[index]);
            return;
        }
        for (int i = amount / coins[index]; i >= 0; i--) {
            recursion(coins, amount - i * coins[index], count + i, index - 1);
        }
    }
}

    /*
    教会我两个事情：（1）不要乱用copyOfRange方法
    （2）对于dfs，关键在于一个void辅助方法的设置，这也是为什么不用int，以及2020.11.22尝试中失败的原因，由于每次都需要返回一个数值，所以不可避免导致
    [186,419,83,408]
6249这个实现不了，必须要可以一直进行遍历操作；
（3）用“原数组 + index 标记可以记录dfs进行到第几步了，这一点和dfs进行层序遍历设置depth 的方法其实是一样一样的”
（4）思路有了，浅层次贪心，深层次是dfs
*/

/*

第二种解法bfs实际上考验的是（1）如何判断有没有经历过这个币，用hashSet直接去重*/
    
    

