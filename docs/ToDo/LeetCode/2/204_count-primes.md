/*
Count the number of prime numbers less than a non-negative number, n.

*/
C  version:


int countPrimes(int n){

    int *nums = malloc(sizeof(int) * n);
    for ( int i = 0; i < n; i++){
        nums[i] = 1;
    }
    for (int i = 2; i <= sqrt(n); i++){
        if (nums[i]){
            int k = 2;
            while (k * i < n){
                nums[k * i] = 0;
                k++;
            }
        }
    }
    int res = 0;
    for (int i =  2; i < n; i++){
        res+= nums[i];
    }
    return res;
}

Java version:
class Solution {
    public int countPrimes(int n) {
        boolean[] isprime=new boolean[n];
        int count=0;
        Arrays.fill(isprime,true);
        for(int i=2;i*i<n;i++){
            if(isprime[i])
            for(int j=i*i;j<n;j+=i){
                isprime[j]=false;
            }
        }
        for(int i=2;i<n;i++){
            if(isprime[i]==true){
                count++;
            }
        }
        return count;
       
    }
}

