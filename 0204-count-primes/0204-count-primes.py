import math
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1]*(n+1)
        for i in range(2,int(math.sqrt(n))+1):
            if(prime[i] == 1):
                for j in range(i*i,n+1,i):
                    prime[j] = 0
        ctr = 0
        for i in range(2,n):
            if prime[i] == 1:
                ctr+=1
        return ctr